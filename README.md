# Logs Analysis - Udacity

This program will analyze a fictional news website database containing over a million rows and answer the following three questions:

1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

This program will run from the command line and it will not take any input from the user.

The database contains newspaper articles, as well as the web server log for the site.
The log has a database row for each time a reader loaded a web page.
The news database has three tables - articles, authors and log.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

Software and files needed and how to install them:

```
Python 2.7.15 - [Python 2.7.15](https://www.python.org/downloads/release/python-2715/)
VirtualBox 5.1 - [VirtualBox 5.1](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1)
Vagrant 2.2.0 - [Vagrant 2.2.0](https://www.vagrantup.com/)
VM Configuration - [Vm Configuration](https://github.com/udacity/fullstack-nanodegree-vm)
News Database - [News Database](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)
reporting_tool.py - [reporting_tool.py](https://github.com/Chrvasq/Logs-Analysis/tree/master)
```

### Installing

A step by step series of examples that tell you how to get a development env running

1. Install VirtualBox

```
VirtualBox is the software that actually runs the virtual machine. You can download it [here](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1). Install the platform package for your operating system. You do not need the extension pack or the SDK. You do not need to launch VirtualBox after installing it; Vagrant will do that.

Currently (November 2018), the supported version of VirtualBox to install is version 5.1. Newer versions do not work with the current release of Vagrant.

**Ubuntu users**: If you are running Ubuntu 14.04, install VirtualBox using the Ubuntu Software Center instead. Due to a reported bug, installing VirtualBox from the site may uninstall other software you need.
```

2. Install Vagrant

```
Vagrant is the software that configures the VM and lets you share files between your host computer and the VM's filesystem. Download it from [here](https://www.vagrantup.com/). Install the version for your operating system.

**Windows users**: The Installer may ask you to grant network permissions to Vagrant or make a firewall exception. Be sure to allow this.
```

3. Download the VM Configuration

```
There are a couple of different ways you can download the VM configuration.

You can download and unzip this file: [FSND-Virtual-Machine.zip](https://s3.amazonaws.com/video.udacity-data.com/topher/2018/April/5acfbfa3_fsnd-virtual-machine/fsnd-virtual-machine.zip) This will give you a directory called FSND-Virtual-Machine. It may be located inside your Downloads folder.

Alternately, you can use Github to fork and clone the repository https://github.com/udacity/fullstack-nanodegree-vm.

Either way, you will end up with a new directory containing the VM files. Change to this directory in your terminal with cd. Inside, you will find another directory called vagrant. Change directory to the vagrant directory.
```

4. Start the virtual machine

```
From your terminal, inside the `vagrant` subdirectory, run the command `vagrant up`. This will cause Vagrant to download the Linux operating system and install it. This may take quite a while (many minutes) depending on how fast your Internet connection is.

When `vagrant up` is finished running, you will get your shell prompt back. At this point, you can run `vagrant ssh` to log in to your newly installed Linux VM.
```

5. Download the news database and load data

```
Download the data [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip). You will need to unzip this file after downloading it. The file inside is called newsdata.sql. Put this file into the `vagrant` directory, which is shared with your virtual machine.

To build the reporting tool, you'll need to load the site's data into your local database.

To load the data, `cd` into the `vagrant` directory and use the command `psql -d news -f newsdata.sql`.
Here's what this command does:

`psql` — the PostgreSQL command line program
`-d news` — connect to the database named news which has been set up for you
`-f newsdata.sql` — run the SQL statements in the file newsdata.sql

Running this command will connect to your installed database server and execute the SQL commands in the downloaded file, creating tables and populating them with data.
```

6. Copy `reporting_tool.py` to `vagrant` subdirectory

```
Copy `reporting_tool.py` to `vagrant` subdirectory.

Next, run the following command to run the program:

`python reporting_tool.py`
```

**Example of output**: 

```
Processing first report...

Top three articles of all time:

"Candidate is jerk, alleges rival" - 338647 views
"Bears love berries, alleges bear" - 253801 views
"Bad things gone, say good people" - 170098 views

Processing second report...

Article authors ranked by views:

Ursula La Multa - 507594 views
Rudolf von Treppenwitz - 423457 views
Anonymous Contributor - 170098 views
Markoff Chaney - 84557 views

Processing third report...

Failed Requests > 1%:

July 17, 2016 - 2.26% errors

End of report.

``` 

## Authors

* **Chris Vasquez** - *Initial work* - [Chris Vasquez](https://github.com/Chrvasq)

## Acknowledgments

* Used README.md template from [PurpleBooth](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2)

