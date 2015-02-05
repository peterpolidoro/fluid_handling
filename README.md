fluid_handling
=====================

Authors:

    Peter Polidoro <polidorop@janelia.hhmi.org>

License:

    BSD

##Installation

###Install Latest Version of Arduino on your Host Machine

<http://arduino.cc/en/Guide/HomePage>

On linux, you may need to add yourself to the group 'dialout' in order
to have write permissions on the USB port:

```shell
sudo usermod -aG dialout <myuser>
```

###Linux and Mac OS X

[Setup Python for Linux](./PYTHON_SETUP_LINUX.md)

[Setup Python for Mac OS X](./PYTHON_SETUP_MAC_OS_X.md)

```shell
mkdir -p ~/virtualenvs/modular_device
virtualenv ~/virtualenvs/modular_device
source ~/virtualenvs/modular_device/bin/activate
pip install modular_device
```

###Windows

[Setup Python for Windows](./PYTHON_SETUP_WINDOWS.md)

```shell
virtualenv C:\virtualenvs\modular_device
C:\virtualenvs\modular_device\Scripts\activate
pip install modular_device
```
