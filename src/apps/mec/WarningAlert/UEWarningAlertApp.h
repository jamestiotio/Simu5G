//
//                  Simu5G
//
// Authors: Giovanni Nardini, Giovanni Stea, Antonio Virdis (University of Pisa)
//
// This file is part of a software released under the license included in file
// "license.pdf". Please read LICENSE and README files before using it.
// The above files and the present reference are part of the software itself,
// and cannot be removed from it.
//

#ifndef __UEWARNINGALERTAPP_H_
#define __UEWARNINGALERTAPP_H_

#include <inet/common/ModuleRefByPar.h>
#include "inet/transportlayer/contract/udp/UdpSocket.h"
#include "inet/networklayer/common/L3Address.h"
#include "inet/networklayer/common/L3AddressResolver.h"

#include "common/binder/Binder.h"

//inet mobility
#include "inet/common/geometry/common/Coord.h"
#include "inet/common/geometry/common/EulerAngles.h"
#include "inet/mobility/contract/IMobility.h"

//WarningAlertPacket
#include "nodes/mec/MECPlatform/MEAppPacket_Types.h"
#include "apps/mec/WarningAlert/packets/WarningAlertPacket_m.h"

namespace simu5g {

using namespace omnetpp;

/**
 * This is a UE app that asks a Device App to instantiate the MECWarningAlertApp.
 * After a successful response, it asks the MEC app to be notified when the car
 * enters a circular zone described by x,y center position and the radius. When a danger
 * event arrives, the car color becomes red.
 *
 * The event behavior flow of the app is:
 * 1) send create MEC app to the Device App
 * 2.1) ACK --> send coordinates to MEC app
 * 2.2) NACK --> do nothing
 * 3) wait for danger events
 * 4) send delete MEC app to the Device App
 */

class UEWarningAlertApp : public cSimpleModule
{

    //communication to device app and mec app
    inet::UdpSocket socket;

    int size_;
    simtime_t period_;
    int localPort_;
    int deviceAppPort_;
    inet::L3Address deviceAppAddress_;

    char *sourceSimbolicAddress;            //Ue[x]
    char *deviceSimbolicAppAddress_;              //meHost.virtualisationInfrastructure

    // MEC application endPoint (returned by the device app)
    inet::L3Address mecAppAddress_;
    int mecAppPort_;

    std::string mecAppName;

    // mobility information
    opp_component_ptr<cModule> ue;
    inet::ModuleRefByPar<inet::IMobility> mobility;
    inet::Coord position;

    //scheduling
    enum MsgKind {
        KIND_SELF_START = 1000,
        KIND_SELF_STOP,
        KIND_SELF_MEC_APP_START,
    };

    cMessage *selfStart_ = nullptr;
    cMessage *selfStop_ = nullptr;

    cMessage *selfMecAppStart_;

    // used to write in a log file
    bool log;

  public:
    ~UEWarningAlertApp();

  protected:

    virtual int numInitStages() const { return inet::NUM_INIT_STAGES; }
    void initialize(int stage);
    virtual void handleMessage(cMessage *msg);
    virtual void finish();

    void sendStartMEWarningAlertApp();
    void sendMessageToMECApp();
    void sendStopMEWarningAlertApp();

    void handleAckStartMEWarningAlertApp(cMessage *msg);
    void handleInfoMEWarningAlertApp(cMessage *msg);
    void handleAckStopMEWarningAlertApp(cMessage *msg);
};

} //namespace

#endif

