# wwcode-kafka
Kafka Women Who Code - August 2018

Author: [@laura_uzcategui](https://twitter.com/laura_uzcategui)

The contents of this repository are for education purposes and were given on talk in Zendesk HQ Dublin in August 2018.

Purpose:
- Standup of a **Single-Node Kafka Cluster** in Docker
- Produce and Send messages with **kafka-python** library

------------
## Initial Setup Overview

The images used for standing up the cluster are coming from :
https://github.com/wurstmeister/kafka-docker

To understand how the kafka cluster is being created checkout:  [docker-compose](./kafka-cluster/docker-compose.yml)

In order to standup a Kafka Cluster you need to have Zookeeper in place, here few reasons why:

- It will store in its Nodes the list of Topics
- It will store also the offsets for each partition/topic
- Leader Election

If you are curious and want to explore more reasons as for why Zookeeper is required by Kafka checkout: [The Role of Zookeeper in Apache Kafka](http://www.waitingforcode.com/apache-kafka/the-role-of-apache-zookeeper-in-apache-kafka/read)

--------------

## Standup your Kafka Cluster in less than 10 seconds

**NOTE**: This cluster is a Kafka single node cluster, if you want to create a multi-broker cluster please checkout: [kafka-docker connectivity guide](https://github.com/wurstmeister/kafka-docker/wiki/Connectivity)

### Standup the cluster

`docker-compose up`

### Check you have the cluster up and running

`docker ps`

You should see an output as follows

```
CONTAINER ID        IMAGE                       COMMAND                  CREATED             STATUS              PORTS                                                NAMES
787134c8e7ec        wurstmeister/kafka:latest   "start-kafka.sh"         21 minutes ago      Up 21 minutes       0.0.0.0:9092->9092/tcp                               kafka-cluster_kafka_1
0c8da2a168f6        wurstmeister/zookeeper      "/bin/sh -c '/usr/sb…"   21 minutes ago      Up 21 minutes       22/tcp, 2888/tcp, 3888/tcp, 0.0.0.0:2181->2181/tcp   kafka-cluster_zookeeper_1
```
---------------
### Setup environment for Producing/Consuming messages

- Go to *producer-consumer* folder

`cd producer-consumer`

- Create a virtualenvironment for python3

`python3 -m venv py3`

- Activate your environment

`source py3/bin/activate`

- Install modules required

`pip install -r requirements.txt`

-------------
### Let's produce  & consume messages

Open 3 terminals and execute the following from each respectively.

`python consumer.py -c 1`

`python consumer.py -c 2`

`python producer.py`

You will see messages flowing from through one producer or another with different partitions.
