#!/usr/bin/env python3

# import the KafkaConsumer
from kafka import KafkaConsumer

import argparse

def consume(consumer_id):
    print("Started consuming from consumer-{}".format(consumer_id))
    # Create a Consumer of twitter_handlers Topic
    tw_consumer = KafkaConsumer(group_id='tw-group',
                                bootstrap_servers='localhost:9092',
                                auto_offset_reset='earliest',
                                consumer_timeout_ms=20000)
    tw_consumer.subscribe('twitter')

    for message in tw_consumer:
        print ("Consumer-{} Topic:{}, Partition:{} Offset:{}: key={} value={}".format(consumer_id,
              message.topic,
              message.partition,
              message.offset,
              message.key,
              message.value)
              )

    tw_consumer.close()

def help_msg():
    return "e.g.: python consumer.py --consumer-id 1"

def main():
    parser = argparse.ArgumentParser(epilog=help_msg())
    parser.add_argument('-c','--consumer-id', default=1, help='Consumer-ID, will identify from where you are consuming from', required=True, type=int, dest='consumer')
    args = parser.parse_args()

    consume(args.consumer)

if __name__ == "__main__":
    main()
