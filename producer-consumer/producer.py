#!/usr/bin/env python3

from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='localhost:9092')

twitter_handlers = ["@WWCodeDublin", "@PyLadiesDublin", "@GDGDublin", "@irelandggd", "@dockerdublin"]

for id, tw_handle in enumerate(twitter_handlers):
    # build a message
    msg = 'Hello Twitter users, follow this awesome accounts: {}, message-counter: {}'.format(tw_handle, id)
    # send a message to the topic
    producer.send(topic='twitter', value=str.encode(msg))

producer.close()
