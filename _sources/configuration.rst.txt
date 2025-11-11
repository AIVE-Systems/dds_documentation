Configuration
=============

Overview
--------

System configuration is managed through TOML files, providing a human-readable format for specifying drone parameters, network settings, and optional hardware configurations. The configuration system includes validation and parsing utilities with both Rust and Python interfaces.

Configuration Structure
-----------------------

A valid configuration file must contain the required ``[drone]`` and ``[network]`` sections, with an optional ``[drop]`` section for payload release functionality.

Required Sections
-----------------

Drone Configuration
~~~~~~~~~~~~~~~~~~~

The ``[drone]`` section specifies aircraft identification and MAVLink connection parameters:

.. code-block:: toml

   [drone]
   asset_type = "STA"
   asset_id = 1
   mavlink_addr = "serial:/dev/ttyACM0:115200"

**Parameters:**

``asset_type`` (string)
   Type of asset.

   - STA
   - FSA
   - MCS
   - FOB
   - FIRE
   - UNDEFINED

``asset_id`` (integer)
   Unique 8-bit numerical identifier for this asset. Must be unique within the asset type class.

``mavlink_addr`` (string)
   MAVLink connection string. See :doc:`mavlink_dds` for valid formats.

Network Configuration
~~~~~~~~~~~~~~~~~~~~~

The ``[network]`` section specifies network topology and peer addresses:

.. code-block:: toml

   [network]
   gateway_ip = "10.0.0.1"
   gateway_comms_port = 8080
   groundstation_ips = ["10.1.0.1", "10.1.0.2", "10.1.0.3"]

**Parameters:**

``gateway_ip`` (string)
   IP address of the network gateway.

``gateway_comms_port`` (integer)
   Port number for gateway to toggle the WiFi network.

``groundstation_ips`` (array of strings)
   List of ground control station IP addresses for communication.

Optional Sections
-----------------

Payload Drop Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~

The ``[drop]`` section configures payload release hardware:

.. code-block:: toml

   [drop]
   servo_id = 23
   pwm_open = 1700

**Parameters:**

``servo_id`` (integer)
   PWM output channel

``pwm_open`` (integer)
   PWM pulse width

See :doc:`drop_payload` for detailed payload drop system documentation.

Configuration Loading
---------------------

Rust Interface
~~~~~~~~~~~~~~

The ``config_reader`` Rust crate provides type-safe configuration loading:

.. code-block:: rust

   use config_reader::Config;

   fn main() -> Result<(), Box<dyn std::error::Error>> {
       let config = Config::from_file("config.toml")?;

       println!("Asset ID: {}", config.drone.asset_id);
       println!("MAVLink: {}", config.drone.mavlink_addr);

       if let Some(drop_config) = config.drop {
           println!("Drop servo: {}", drop_config.servo_id);
       }

       Ok(())
   }

Python Interface
~~~~~~~~~~~~~~~~

Python bindings enable configuration loading from Python applications:

.. code-block:: python

   from config_reader import load_config

   config = load_config("config.toml")

   print(f"Asset ID: {config["drone"]["asset_id"]}")
   print(f"MAVLink: {config["drone"]["mavlink_addr"]}")

   if config.drop:
       print(f"Drop servo: {config["drop"]["servo_id"]}")


Troubleshooting
---------------

**Configuration Not Found:**

Ensure the configuration file path is correct and the file is readable by the application.

**Validation Errors:**

Check error messages for specific field issues. Common problems:

- Missing required sections
- Typos in field names
- Incorrect data types
- Invalid MAVLink address format

**Network Configuration Issues:**

Verify IP addresses are reachable and ports are not blocked by firewalls.

**Serial Port Access:**

On Linux, ensure the user has permission to access serial devices:

.. code-block:: bash

   sudo usermod -a -G dialout $USER
   # Log out and back in for changes to take effect
