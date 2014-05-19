# Vagrant Serf Demo and serf-python example

This demo provides a very simple Vagrantfile that creates three nodes
("172.20.20.10", "172.20.20.11", "172.20.20.13"). All of these are running
a standard Ubuntu 12.04 distribution, and Serf is pre-installed.

Also provided serf-python examples (dependencies also installed)

To get started, you can start the cluster by just doing:

    $ vagrant up

Once it is finished, you should be able to see the following:

    $ vagrant status
    Current machine states:
    n1                        running
    n2                        running
    n3                        running

At this point the three nodes are running and you can SSH in to play with them:

    $ vagrant ssh n1
    ...
    $ vagrant ssh n2
    ...
    $ vagrant ssh n3
    ...

To learn more about starting serf, joining nodes and interacting with the agent,
checkout the [getting started guide](http://www.serfdom.io/intro/getting-started/install.html).

More about serf-python at [serf-python](https://github.com/spikeekips/serf-python)
