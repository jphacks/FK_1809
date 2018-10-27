require 'sinatra'
require 'json'

post '/' do
  words = ['今日は良い服ですね',
            '昨日と同じ服ではありませんか',
            'おしゃれな服ですね',
            'まあまあです',
            'お友達と被っています']
  word = words[rand(words.length-1)]

  return {
      "version": "1.0",
      "response": {
          "outputSpeech": {
              "type": "SpeechList",
              "values": [
                  {
                      "type":"PlainText",
                      "lang":"ja",
                      "value": word
                  }
              ]
          },
          "card": {},
          "directives": [],
          "shouldEndSession": true
      }
  }.to_json
end