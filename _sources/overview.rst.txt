Overview
========

Introduction
------------

This documentation describes a distributed communication infrastructure designed for multi-drone systems. The architecture enables scalable, real-time coordination of drone swarms through a publish-subscribe middleware layer.

What is DDS?
------------

The Data Distribution Service (DDS) is a middleware protocol providing data-centric connectivity between distributed applications. Unlike traditional client-server architectures, DDS uses a publish-subscribe model where:

- **Publishers** send data to topics without knowing who receives it
- **Subscribers** receive data from topics without knowing the source
- **Topics** act as logical channels for typed data
- **Discovery** happens automatically without central coordination

This decentralised approach scales naturally as system complexity grows, making it ideal for multi-agent systems.

Why DDS for Drone Swarms?
--------------------------

Traditional point-to-point communication becomes unmanageable as the number of agents increases. DDS solves this by:

**Decoupling**
   Drones and ground stations communicate through topics, not direct connections. Adding new agents requires no reconfiguration.

**Scalability**
   The architecture naturally scales from a single drone to hundreds of agents without architectural changes.

**Reliability**
   Configurable Quality of Service (QoS) policies ensure critical data delivery whilst optimising bandwidth usage.

**Interoperability**
   Heterogeneous systems communicate through standardised interfaces.

**Real-time Performance**
   Low-latency communication suitable for control loops and time-critical coordination.

Our Implementation
------------------

We use **Zenoh** as our DDS implementation—a modern, high-performance middleware with native Rust support. Zenoh provides pub-sub, querying, and storage capabilities whilst maintaining compatibility with DDS standards.

Messages are serialised using **FlatBuffers**, enabling zero-copy access to data with strong typing and cross-language support.

System Components
-----------------

The platform consists of several integrated components:

**MAVLink-DDS Bridge**
   Connects flight controllers running ArduPilot to the DDS, translating between MAVLink and DDS topics.

**Message Library**
   Provides standardised FlatBuffer message definitions and codec utilities for type-safe communication.

**Configuration System**
   TOML-based configuration management for per-drone settings and network parameters.

Documentation Structure
-----------------------

This documentation is organised as follows:

:doc:`architecture`
   System architecture overview, topic hierarchy, and design principles.

:doc:`mavlink_dds`
   MAVLink-DDS bridge node implementation, including payload drop functionality.

:doc:`configuration`
   Configuration file format and management system.

:doc:`serialisation`
   Message serialisation using FlatBuffers and the message library.
