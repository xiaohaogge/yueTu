
import json

str = 'sifsldgj false'

s = str.replace('false','True')
print(str)
print(s)



ss = '''{
  "baseResponse": {
    "cid": "qunarytb",
    "message": "success",
    "pid": "",
    "status": 200,
    "traceId": "99b6660f-ac71-4a10-8745-dcc9b4cf1e76",
    "nima":false
  },
  "routing": [
    {
      "accountCode": "",
      "aduTag": "",
      "adultPrice": 671.7839591532816,
      "adultPublishPrice": 655.4842,
      "adultPublishTax": 0,
      "adultTax": 1,
      "adultTaxType": 0,
      "adultType": "",
      "adultUoTax": 0,
      "adultYqTax": 0,
      "adultYrTax": 0,
      "applyType": 0,
      "arf": "",
      "bookingToken": "AtzqsvodMGctV-A5Ttvb0bOtyCkujfOp2LwhFLZEev5VENuR2RoUuJ6xhgZ2zRFwBVCTEf2MmlLulbvz5F0HPOAtIzRt1Lo63lPpQTMFX4vGUHYi_wzl1OLtNxo-01iUGOobg7v9sjyaRfSC58wCd7dZtgnDK6cyxNXrPDG0YZGiiidaCvQzX-Z-BHajEDs1eaW5VecKj_LqrAP2QyEubU3cgsC9ZOYgvKrA5oKrIY48FeTgQ2tKScvaCw-pDLKJicEKQO44aot1xh9ITlYFWaCf2hkqETU_Gq6GG-tkJ-CaZiVMRASiATr5tGKWfm9UopQjy0MN-_1mbmKYbjdO1JdKMBKR2C20DfLrOq9CSHEwm0CTtNgZuWCUJGINOVlqsD2Lyed8fVRxbooKqxbnfdecaRj7GBwjJWiJO5JBl6UkIdGip5Z7swZIMKStXQrXgAX2qEqeWbOtNB0oxtahN6A==",
      "cabin": "E",
      "chiTag": "",
      "childFareBasis": "",
      "childPrice": 671.7839591532816,
      "childPublishPrice": 655.4842,
      "childPublishTax": 0,
      "childTax": 1,
      "childTaxType": 0,
      "childTicketPrice": 0,
      "childType": "",
      "childUoTax": 0,
      "childYqTax": 0,
      "childYrTax": 0,
      "ctof": "",
      "currency": "CNY",
      "currencyConversions": [
        {
          "from": "EUR",
          "rate": 7.8974,
          "source": "BOC",
          "timestamp": "2019-08-23T00:37:25Z",
          "to": "CNY"
        },
        {
          "from": "USD",
          "rate": 7,
          "source": "MANUAL",
          "timestamp": "2019-08-14T07:46:00Z",
          "to": "CNY"
        }
      ],
      "data": "99b6660f-ac71-4a10-8745-dcc9b4cf1e76#4139757f-a9e1-45e8-93da-dbe5af92b511#RS502_E",
      "eligibility": "",
      "evictionMarks": [
        {
          "evictionReason": "Platform[去哪人商旅] 航程内拼接",
          "traceSpans": [
            {
              "application": "night-king",
              "createdAt": null,
              "desc": "PlatformConfig filter",
              "spanId": "",
              "tags": {
                "DisplayNumber": "PFC1907306359",
                "Revision": "5"
              },
              "traceType": "None"
            }
          ]
        }
      ],
      "fareBasis": "",
      "fareCalcLine": "",
      "fareType": "PRIVATE",
      "flightCode": "",
      "infantPrice": 0,
      "infantPublishPrice": 0,
      "infantPublishTax": 0,
      "infantTax": 0,
      "infantTaxType": 0,
      "infantType": "",
      "itinerary": [
        {
          "destinationCity": "SEL",
          "duration": 13200,
          "originCity": "HKG",
          "segment": [
            {
              "accountCode": "",
              "aircraftCode": "",
              "arrivalAirport": "ICN",
              "arrivalTerminal": "",
              "arrivalTime": "201909230530",
              "arrivalTimeWithOffset": "",
              "availabilitySource": "",
              "baggage": {
                "baggageCheck": false,
                "freeBaggagePiece": -1,
                "freeBaggageWeight": 0
              },
              "bookingClass": "X",
              "cabin": "E",
              "carrier": "RS",
              "childCabin": "",
              "childFareBasis": "",
              "codeShare": false,
              "connection": false,
              "departureAirport": "HKG",
              "departureTerminal": "",
              "departureTime": "201909230050",
              "departureTimeWithOffset": "",
              "duration": 220,
              "fareBasis": "",
              "fareType": "PRIVATE",
              "flightNumber": "RS502",
              "flyTime": 0,
              "key": "",
              "mainSegment": true,
              "marriageGrp": "",
              "operatingCarrier": "",
              "operatingFlightNumber": "",
              "seats": 1,
              "status": "",
              "stopCity": [],
              "stopInfo": 0
            }
          ],
          "segmentSplicing": true
        }
      ],
      "itinerarySplicing": false,
      "masterCurrency": "CNY",
      "multiTicket": false,
      "nationalType": 0,
      "nationality": "",
      "onlineCheckIn": false,
      "oriAdultPrice": 83,
      "oriAdultTax": 0,
      "oriChildPrice": 83,
      "oriChildTax": 0,
      "oriInfantPrice": 0,
      "oriInfantTax": 0,
      "policyPriceChanges": [
        {
          "adultChange": {
            "absChange": {
              "amount": 4,
              "currency": "USD"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 0
            },
            "totalChange": {
              "amount": -28,
              "currency": "CNY"
            }
          },
          "childChange": {
            "absChange": {
              "amount": 4,
              "currency": "USD"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 0
            },
            "totalChange": {
              "amount": -28,
              "currency": "CNY"
            }
          },
          "displayNumber": "IC1908021687",
          "infantChange": null,
          "isFeeApplyToProvider": true,
          "otherAbsChangeDetails": [
            {
              "absTotal": {
                "amount": 5,
                "currency": "USD"
              },
              "desc": "INCENTIVE_RECEIVABLE",
              "totalChange": {
                "amount": 35,
                "currency": "CNY"
              }
            }
          ],
          "otherPercentageChangeDetails": [],
          "policyDesc": "IncentivePolicy:IC1908021687",
          "policyId": "5d4411fa73e1340001e3e890",
          "policyType": "INCENTIVE"
        },
        {
          "adultChange": {
            "absChange": {
              "amount": 5,
              "currency": "CNY"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 5.99
            },
            "totalChange": {
              "amount": 45.29975915328156,
              "currency": "CNY"
            }
          },
          "childChange": {
            "absChange": {
              "amount": 5,
              "currency": "CNY"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 5.99
            },
            "totalChange": {
              "amount": 45.29975915328156,
              "currency": "CNY"
            }
          },
          "displayNumber": "PF1907210860",
          "infantChange": {
            "absChange": {
              "amount": 5,
              "currency": "CNY"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 5.99
            },
            "totalChange": {
              "amount": 5.318583129454313,
              "currency": "CNY"
            }
          },
          "isFeeApplyToProvider": true,
          "otherAbsChangeDetails": [],
          "otherPercentageChangeDetails": [],
          "policyDesc": "PlatformPolicy:PF1907210860",
          "policyId": "5d342d9bf24d1c0001195a24",
          "policyType": "PLATFORM"
        }
      ],
      "posLocation": "CN",
      "priceType": 0,
      "providerCurrency": "EUR",
      "providerName": "skypk",
      "providerType": "PROVIDER_API",
      "routingId": "",
      "rule": {
        "changeBeforeDep": 0,
        "changeBeforeDepFee": 0,
        "changeDetail": null,
        "cnRemark": "",
        "currency": "CNY",
        "enRemark": "",
        "manualFareRule": null,
        "miniRule": -404,
        "noShowChange": 0,
        "noShowChangeAfter": 0,
        "noShowChangeAfterFee": 0,
        "noShowChangeFee": 0,
        "noShowRefund": 0,
        "noShowRefundAfter": 0,
        "noShowRefundAfterFee": 0,
        "noShowRefundFee": 0,
        "originRuleFee": {
          "changeAfterFee": -404,
          "changeAfterNoshowFee": -404,
          "changeBeforeFee": -404,
          "changeBeforeNoshowFee": -404,
          "currency": "",
          "refundAfterFee": -404,
          "refundAfterNoshowFee": -404,
          "refundBeforeFee": -404,
          "refundBeforeNoshowFee": -404
        },
        "partEndorse": 0,
        "partEndorsePrice": 0,
        "partRefund": 0,
        "partRefundFee": 0,
        "refundBeforeDep": 0,
        "refundBeforeDepFee": 0,
        "ruleFromOta": -404,
        "useOld": false
      },
      "saleBaggage": false,
      "seats": 1,
      "suitAge": "",
      "ticketInvoiceType": 0,
      "ticketPrice": 0,
      "ticketSource": 0,
      "ticketTimeLimitMinutes": 2880,
      "tof": "",
      "traceSpans": [
        {
          "application": "night-king",
          "createdAt": "2019-08-23T00:51:25.204008945Z",
          "desc": "move amount of 1.000000 from fare price to adult tax",
          "spanId": "dac58fab-849d-401c-a806-7e520996f1ff",
          "tags": {},
          "traceType": "None"
        },
        {
          "application": "night-king",
          "createdAt": "2019-08-23T00:51:25.204012392Z",
          "desc": "move amount of 1.000000 from child fare price to child tax",
          "spanId": "4170b9eb-18e8-4c83-82ab-0899652e68f4",
          "tags": {},
          "traceType": "None"
        }
      ],
      "validSegmentsCount": 1,
      "validatingCarrier": "RS",
      "viewPrice": 0
    },
    {
      "accountCode": "",
      "aduTag": "",
      "adultPrice": 705.3863418785236,
      "adultPublishPrice": 687.0738,
      "adultPublishTax": 0,
      "adultTax": 1,
      "adultTaxType": 0,
      "adultType": "",
      "adultUoTax": 0,
      "adultYqTax": 0,
      "adultYrTax": 0,
      "applyType": 0,
      "arf": "",
      "bookingToken": "A8bR7X8X2uS4c1QsiUOhCULz1Owvqer3aQk9RieN9kPWWz6L7GBlRRJAA7BVmwDGqujCopxoaadsHyRbnDLKA36dimZMavwYaLW-WdUOgZcNODbGR-QITEK1ViEec-0LA98iMB3LGAcRpxhY3kBFEp2wABR2rl2bkEa7dvJXy3PARJFNdQN2jBrlt3nktj3hCm0PvT8L7_uEIZEQfdIq2_vypM7IUIlMDrhMPyVCw34cMbPjkJQslBtlWCNvOeOjG_q3UUyj7IIPA9LI8Dbut_sE4g49C7otSM0TF14VkVZ7t-Lg1RMx5m8DdqlHSHNpi-jHYllt9p77HrbUbVOSxyNLXL6c-6hzbeiCsc7u01-MbJFezzGJD6_BGXuIUuDO15RKcneOT-Wz1xzvrJ3vo0mHubEpIC7wtDVSwHpNZyv0zWQaVkWeZclxMq5HlyW6k",
      "cabin": "E",
      "chiTag": "",
      "childFareBasis": "",
      "childPrice": 705.3863418785236,
      "childPublishPrice": 687.0738,
      "childPublishTax": 0,
      "childTax": 1,
      "childTaxType": 0,
      "childTicketPrice": 0,
      "childType": "",
      "childUoTax": 0,
      "childYqTax": 0,
      "childYrTax": 0,
      "ctof": "",
      "currency": "CNY",
      "currencyConversions": [
        {
          "from": "EUR",
          "rate": 7.8974,
          "source": "BOC",
          "timestamp": "2019-08-23T00:37:25Z",
          "to": "CNY"
        },
        {
          "from": "USD",
          "rate": 7,
          "source": "MANUAL",
          "timestamp": "2019-08-14T07:46:00Z",
          "to": "CNY"
        }
      ],
      "data": "99b6660f-ac71-4a10-8745-dcc9b4cf1e76#3334fc64-ba07-4ade-9496-b59998d1259c#7C2108_E",
      "eligibility": "",
      "evictionMarks": [
        {
          "evictionReason": "Platform[去哪人商旅] 航程内拼接",
          "traceSpans": [
            {
              "application": "night-king",
              "createdAt": null,
              "desc": "PlatformConfig filter",
              "spanId": "",
              "tags": {
                "DisplayNumber": "PFC1907306359",
                "Revision": "5"
              },
              "traceType": "None"
            }
          ]
        }
      ],
      "fareBasis": "",
      "fareCalcLine": "",
      "fareType": "PRIVATE",
      "flightCode": "",
      "infantPrice": 0,
      "infantPublishPrice": 0,
      "infantPublishTax": 0,
      "infantTax": 0,
      "infantTaxType": 0,
      "infantType": "",
      "itinerary": [
        {
          "destinationCity": "SEL",
          "duration": 12900,
          "originCity": "HKG",
          "segment": [
            {
              "accountCode": "",
              "aircraftCode": "",
              "arrivalAirport": "ICN",
              "arrivalTerminal": "",
              "arrivalTime": "201909230600",
              "arrivalTimeWithOffset": "",
              "availabilitySource": "",
              "baggage": {
                "baggageCheck": false,
                "freeBaggagePiece": -1,
                "freeBaggageWeight": 0
              },
              "bookingClass": "S",
              "cabin": "E",
              "carrier": "7C",
              "childCabin": "",
              "childFareBasis": "",
              "codeShare": false,
              "connection": false,
              "departureAirport": "HKG",
              "departureTerminal": "",
              "departureTime": "201909230125",
              "departureTimeWithOffset": "",
              "duration": 215,
              "fareBasis": "",
              "fareType": "PRIVATE",
              "flightNumber": "7C2108",
              "flyTime": 0,
              "key": "",
              "mainSegment": true,
              "marriageGrp": "",
              "operatingCarrier": "",
              "operatingFlightNumber": "",
              "seats": 1,
              "status": "",
              "stopCity": [],
              "stopInfo": 0
            }
          ],
          "segmentSplicing": true
        }
      ],
      "itinerarySplicing": false,
      "masterCurrency": "CNY",
      "multiTicket": false,
      "nationalType": 0,
      "nationality": "",
      "onlineCheckIn": false,
      "oriAdultPrice": 87,
      "oriAdultTax": 0,
      "oriChildPrice": 87,
      "oriChildTax": 0,
      "oriInfantPrice": 0,
      "oriInfantTax": 0,
      "policyPriceChanges": [
        {
          "adultChange": {
            "absChange": {
              "amount": 4,
              "currency": "USD"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 0
            },
            "totalChange": {
              "amount": -28,
              "currency": "CNY"
            }
          },
          "childChange": {
            "absChange": {
              "amount": 4,
              "currency": "USD"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 0
            },
            "totalChange": {
              "amount": -28,
              "currency": "CNY"
            }
          },
          "displayNumber": "IC1908021687",
          "infantChange": null,
          "isFeeApplyToProvider": true,
          "otherAbsChangeDetails": [
            {
              "absTotal": {
                "amount": 5,
                "currency": "USD"
              },
              "desc": "INCENTIVE_RECEIVABLE",
              "totalChange": {
                "amount": 35,
                "currency": "CNY"
              }
            }
          ],
          "otherPercentageChangeDetails": [],
          "policyDesc": "IncentivePolicy:IC1908021687",
          "policyId": "5d4411fa73e1340001e3e890",
          "policyType": "INCENTIVE"
        },
        {
          "adultChange": {
            "absChange": {
              "amount": 5,
              "currency": "CNY"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 5.99
            },
            "totalChange": {
              "amount": 47.31254187852356,
              "currency": "CNY"
            }
          },
          "childChange": {
            "absChange": {
              "amount": 5,
              "currency": "CNY"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 5.99
            },
            "totalChange": {
              "amount": 47.31254187852356,
              "currency": "CNY"
            }
          },
          "displayNumber": "PF1907210860",
          "infantChange": {
            "absChange": {
              "amount": 5,
              "currency": "CNY"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 5.99
            },
            "totalChange": {
              "amount": 5.318583129454313,
              "currency": "CNY"
            }
          },
          "isFeeApplyToProvider": true,
          "otherAbsChangeDetails": [],
          "otherPercentageChangeDetails": [],
          "policyDesc": "PlatformPolicy:PF1907210860",
          "policyId": "5d342d9bf24d1c0001195a24",
          "policyType": "PLATFORM"
        }
      ],
      "posLocation": "CN",
      "priceType": 0,
      "providerCurrency": "EUR",
      "providerName": "skypk",
      "providerType": "PROVIDER_API",
      "routingId": "",
      "rule": {
        "changeBeforeDep": 0,
        "changeBeforeDepFee": 0,
        "changeDetail": null,
        "cnRemark": "",
        "currency": "CNY",
        "enRemark": "",
        "manualFareRule": null,
        "miniRule": 0,
        "noShowChange": 0,
        "noShowChangeAfter": 0,
        "noShowChangeAfterFee": 0,
        "noShowChangeFee": 0,
        "noShowRefund": 0,
        "noShowRefundAfter": 0,
        "noShowRefundAfterFee": 0,
        "noShowRefundFee": 0,
        "originRuleFee": {
          "changeAfterFee": -404,
          "changeAfterNoshowFee": -404,
          "changeBeforeFee": -404,
          "changeBeforeNoshowFee": -404,
          "currency": "",
          "refundAfterFee": -404,
          "refundAfterNoshowFee": -404,
          "refundBeforeFee": -404,
          "refundBeforeNoshowFee": -404
        },
        "partEndorse": 0,
        "partEndorsePrice": 0,
        "partRefund": 0,
        "partRefundFee": 0,
        "refundBeforeDep": 0,
        "refundBeforeDepFee": 0,
        "ruleFromOta": 0,
        "useOld": false
      },
      "saleBaggage": true,
      "seats": 1,
      "suitAge": "",
      "ticketInvoiceType": 0,
      "ticketPrice": 0,
      "ticketSource": 0,
      "ticketTimeLimitMinutes": 2880,
      "tof": "",
      "traceSpans": [
        {
          "application": "night-king",
          "createdAt": "2019-08-23T00:51:25.204640883Z",
          "desc": "move amount of 1.000000 from fare price to adult tax",
          "spanId": "54eabb84-8903-4c3d-a605-9df5e061a971",
          "tags": {},
          "traceType": "None"
        },
        {
          "application": "night-king",
          "createdAt": "2019-08-23T00:51:25.204644227Z",
          "desc": "move amount of 1.000000 from child fare price to child tax",
          "spanId": "45bacb4c-0518-426a-8394-563b76235f60",
          "tags": {},
          "traceType": "None"
        }
      ],
      "validSegmentsCount": 1,
      "validatingCarrier": "7C",
      "viewPrice": 0
    },
    {
      "accountCode": "",
      "aduTag": "",
      "adultPrice": 780.991703010318,
      "adultPublishPrice": 758.1504,
      "adultPublishTax": 0,
      "adultTax": 1,
      "adultTaxType": 0,
      "adultType": "",
      "adultUoTax": 0,
      "adultYqTax": 0,
      "adultYrTax": 0,
      "applyType": 0,
      "arf": "",
      "bookingToken": "APhTPH4oze8w4ZoyLADLty1FDEFDpaYLI_s25Q08cTsxLtmtbbDUGWN2BnJylwQhtEupx_KCODxe8d4sOQvcRr9fwK2juaMqI32wYBM_gviZrnpmi515Wo6HEKYd8m8FoLWrsj96DGGWIM9nzy5klL-JxQtBQdRm5K8rcsV8qfk40lY3RWP7myohvUlaJ6IdVNjZv2dM-bKZioeKivz_7K9p0gl899F5cpJznWbZV3DRMvfr98X8cUeZHHoG3DVZzv-Le6h4acgVFMRZ7JI1xJGwsVpDhdyuMCvrcItcdod8N2nVHaS9yIkJ7uVVjUZVz2J-Ke317zalTisMa3vgXFnOkHPQkDrO6-LmQD9FzXuRCCTlQA5S0tjHlUso0b0QzX73bmu7bvh7TPDRxBr9CEzhxCtUf7aBSktgbbisiZbhCt9s-zFMVAXfWB0UpTvvO",
      "cabin": "E",
      "chiTag": "",
      "childFareBasis": "",
      "childPrice": 780.991703010318,
      "childPublishPrice": 758.1504,
      "childPublishTax": 0,
      "childTax": 1,
      "childTaxType": 0,
      "childTicketPrice": 0,
      "childType": "",
      "childUoTax": 0,
      "childYqTax": 0,
      "childYrTax": 0,
      "ctof": "",
      "currency": "CNY",
      "currencyConversions": [
        {
          "from": "EUR",
          "rate": 7.8974,
          "source": "BOC",
          "timestamp": "2019-08-23T00:37:25Z",
          "to": "CNY"
        },
        {
          "from": "USD",
          "rate": 7,
          "source": "MANUAL",
          "timestamp": "2019-08-14T07:46:00Z",
          "to": "CNY"
        }
      ],
      "data": "99b6660f-ac71-4a10-8745-dcc9b4cf1e76#1e448d2c-1f5c-477b-a22d-cc6197899753#7C2102_E",
      "eligibility": "",
      "evictionMarks": [
        {
          "evictionReason": "Platform[去哪人商旅] 航程内拼接",
          "traceSpans": [
            {
              "application": "night-king",
              "createdAt": null,
              "desc": "PlatformConfig filter",
              "spanId": "",
              "tags": {
                "DisplayNumber": "PFC1907306359",
                "Revision": "5"
              },
              "traceType": "None"
            }
          ]
        }
      ],
      "fareBasis": "",
      "fareCalcLine": "",
      "fareType": "PRIVATE",
      "flightCode": "",
      "infantPrice": 0,
      "infantPublishPrice": 0,
      "infantPublishTax": 0,
      "infantTax": 0,
      "infantTaxType": 0,
      "infantType": "",
      "itinerary": [
        {
          "destinationCity": "SEL",
          "duration": 13200,
          "originCity": "HKG",
          "segment": [
            {
              "accountCode": "",
              "aircraftCode": "",
              "arrivalAirport": "ICN",
              "arrivalTerminal": "",
              "arrivalTime": "201909231815",
              "arrivalTimeWithOffset": "",
              "availabilitySource": "",
              "baggage": {
                "baggageCheck": false,
                "freeBaggagePiece": -1,
                "freeBaggageWeight": 0
              },
              "bookingClass": "S",
              "cabin": "E",
              "carrier": "7C",
              "childCabin": "",
              "childFareBasis": "",
              "codeShare": false,
              "connection": false,
              "departureAirport": "HKG",
              "departureTerminal": "",
              "departureTime": "201909231335",
              "departureTimeWithOffset": "",
              "duration": 220,
              "fareBasis": "",
              "fareType": "PRIVATE",
              "flightNumber": "7C2102",
              "flyTime": 0,
              "key": "",
              "mainSegment": true,
              "marriageGrp": "",
              "operatingCarrier": "",
              "operatingFlightNumber": "",
              "seats": 1,
              "status": "",
              "stopCity": [],
              "stopInfo": 0
            }
          ],
          "segmentSplicing": true
        }
      ],
      "itinerarySplicing": false,
      "masterCurrency": "CNY",
      "multiTicket": false,
      "nationalType": 0,
      "nationality": "",
      "onlineCheckIn": false,
      "oriAdultPrice": 96,
      "oriAdultTax": 0,
      "oriChildPrice": 96,
      "oriChildTax": 0,
      "oriInfantPrice": 0,
      "oriInfantTax": 0,
      "policyPriceChanges": [
        {
          "adultChange": {
            "absChange": {
              "amount": 4,
              "currency": "USD"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 0
            },
            "totalChange": {
              "amount": -28,
              "currency": "CNY"
            }
          },
          "childChange": {
            "absChange": {
              "amount": 4,
              "currency": "USD"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 0
            },
            "totalChange": {
              "amount": -28,
              "currency": "CNY"
            }
          },
          "displayNumber": "IC1908021687",
          "infantChange": null,
          "isFeeApplyToProvider": true,
          "otherAbsChangeDetails": [
            {
              "absTotal": {
                "amount": 5,
                "currency": "USD"
              },
              "desc": "INCENTIVE_RECEIVABLE",
              "totalChange": {
                "amount": 35,
                "currency": "CNY"
              }
            }
          ],
          "otherPercentageChangeDetails": [],
          "policyDesc": "IncentivePolicy:IC1908021687",
          "policyId": "5d4411fa73e1340001e3e890",
          "policyType": "INCENTIVE"
        },
        {
          "adultChange": {
            "absChange": {
              "amount": 5,
              "currency": "CNY"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 5.99
            },
            "totalChange": {
              "amount": 51.84130301031805,
              "currency": "CNY"
            }
          },
          "childChange": {
            "absChange": {
              "amount": 5,
              "currency": "CNY"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 5.99
            },
            "totalChange": {
              "amount": 51.84130301031805,
              "currency": "CNY"
            }
          },
          "displayNumber": "PF1907210860",
          "infantChange": {
            "absChange": {
              "amount": 5,
              "currency": "CNY"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 5.99
            },
            "totalChange": {
              "amount": 5.318583129454313,
              "currency": "CNY"
            }
          },
          "isFeeApplyToProvider": true,
          "otherAbsChangeDetails": [],
          "otherPercentageChangeDetails": [],
          "policyDesc": "PlatformPolicy:PF1907210860",
          "policyId": "5d342d9bf24d1c0001195a24",
          "policyType": "PLATFORM"
        }
      ],
      "posLocation": "CN",
      "priceType": 0,
      "providerCurrency": "EUR",
      "providerName": "skypk",
      "providerType": "PROVIDER_API",
      "routingId": "",
      "rule": {
        "changeBeforeDep": 0,
        "changeBeforeDepFee": 0,
        "changeDetail": null,
        "cnRemark": "",
        "currency": "CNY",
        "enRemark": "",
        "manualFareRule": null,
        "miniRule": 0,
        "noShowChange": 0,
        "noShowChangeAfter": 0,
        "noShowChangeAfterFee": 0,
        "noShowChangeFee": 0,
        "noShowRefund": 0,
        "noShowRefundAfter": 0,
        "noShowRefundAfterFee": 0,
        "noShowRefundFee": 0,
        "originRuleFee": {
          "changeAfterFee": -404,
          "changeAfterNoshowFee": -404,
          "changeBeforeFee": -404,
          "changeBeforeNoshowFee": -404,
          "currency": "",
          "refundAfterFee": -404,
          "refundAfterNoshowFee": -404,
          "refundBeforeFee": -404,
          "refundBeforeNoshowFee": -404
        },
        "partEndorse": 0,
        "partEndorsePrice": 0,
        "partRefund": 0,
        "partRefundFee": 0,
        "refundBeforeDep": 0,
        "refundBeforeDepFee": 0,
        "ruleFromOta": 0,
        "useOld": false
      },
      "saleBaggage": true,
      "seats": 1,
      "suitAge": "",
      "ticketInvoiceType": 0,
      "ticketPrice": 0,
      "ticketSource": 0,
      "ticketTimeLimitMinutes": 2880,
      "tof": "",
      "traceSpans": [
        {
          "application": "night-king",
          "createdAt": "2019-08-23T00:51:25.204690044Z",
          "desc": "move amount of 1.000000 from fare price to adult tax",
          "spanId": "cf1733e5-ca45-4536-9f59-5983340d094e",
          "tags": {},
          "traceType": "None"
        },
        {
          "application": "night-king",
          "createdAt": "2019-08-23T00:51:25.204693190Z",
          "desc": "move amount of 1.000000 from child fare price to child tax",
          "spanId": "b44b607f-ebae-4fbe-b466-69d5bddc562b",
          "tags": {},
          "traceType": "None"
        }
      ],
      "validSegmentsCount": 1,
      "validatingCarrier": "7C",
      "viewPrice": 0
    },
    {
      "accountCode": "",
      "aduTag": "",
      "adultPrice": 789.3922986916286,
      "adultPublishPrice": 766.0478,
      "adultPublishTax": 0,
      "adultTax": 1,
      "adultTaxType": 0,
      "adultType": "",
      "adultUoTax": 0,
      "adultYqTax": 0,
      "adultYrTax": 0,
      "applyType": 0,
      "arf": "",
      "bookingToken": "A4c_ht_n4Bx6mc_7LgcCQbqqhfZWm9gCHsEEHNkW5AkZDZN8uHKad1jijJ6WjNC2dYKta39s2bsz4X8HD6DCaeDfl4PCgtZciOlatQYYikgokF9hwCckSg8FCk-wQbYiibGDDnS5_XwA0P_G5CENpJpb7QHSNOHuHpb4CvafDJlLU3dQWQQYVNuir0FAeJhrZlWv20OAXDQxSkJ3vSNmChFZT-7Xmo-4L-FuMjXl11ymLBlr1b5oWU2Q4GqvejCZo4g2NQ3dcnOTryezIPlCum_kfBIuPK2XeQELjr92zrQj7QlHN5F9wduhfmJfJOzvk_eVmtMyKRSwWVb9cjXmgbeE_mgSZ8RuyIrol1pf-NPbb75hq9Y_hgZgIts6IskTgniBSMilSeUYJKvRLH_Ls3XdU8-FTiT2V0tOoNBiHMSngqe4A8gsI4Ht_xRKPWckT",
      "cabin": "E",
      "chiTag": "",
      "childFareBasis": "",
      "childPrice": 789.3922986916286,
      "childPublishPrice": 766.0478,
      "childPublishTax": 0,
      "childTax": 1,
      "childTaxType": 0,
      "childTicketPrice": 0,
      "childType": "",
      "childUoTax": 0,
      "childYqTax": 0,
      "childYrTax": 0,
      "ctof": "",
      "currency": "CNY",
      "currencyConversions": [
        {
          "from": "EUR",
          "rate": 7.8974,
          "source": "BOC",
          "timestamp": "2019-08-23T00:37:25Z",
          "to": "CNY"
        },
        {
          "from": "USD",
          "rate": 7,
          "source": "MANUAL",
          "timestamp": "2019-08-14T07:46:00Z",
          "to": "CNY"
        }
      ],
      "data": "99b6660f-ac71-4a10-8745-dcc9b4cf1e76#70834e71-8029-49c0-8598-134c1761aff3#UO626_E",
      "eligibility": "",
      "evictionMarks": [
        {
          "evictionReason": "Platform[去哪人商旅] 航程内拼接",
          "traceSpans": [
            {
              "application": "night-king",
              "createdAt": null,
              "desc": "PlatformConfig filter",
              "spanId": "",
              "tags": {
                "DisplayNumber": "PFC1907306359",
                "Revision": "5"
              },
              "traceType": "None"
            }
          ]
        }
      ],
      "fareBasis": "",
      "fareCalcLine": "",
      "fareType": "PRIVATE",
      "flightCode": "",
      "infantPrice": 0,
      "infantPublishPrice": 0,
      "infantPublishTax": 0,
      "infantTax": 0,
      "infantTaxType": 0,
      "infantType": "",
      "itinerary": [
        {
          "destinationCity": "SEL",
          "duration": 13800,
          "originCity": "HKG",
          "segment": [
            {
              "accountCode": "",
              "aircraftCode": "",
              "arrivalAirport": "ICN",
              "arrivalTerminal": "",
              "arrivalTime": "201909232135",
              "arrivalTimeWithOffset": "",
              "availabilitySource": "",
              "baggage": {
                "baggageCheck": false,
                "freeBaggagePiece": -1,
                "freeBaggageWeight": 0
              },
              "bookingClass": "W",
              "cabin": "E",
              "carrier": "UO",
              "childCabin": "",
              "childFareBasis": "",
              "codeShare": false,
              "connection": false,
              "departureAirport": "HKG",
              "departureTerminal": "",
              "departureTime": "201909231645",
              "departureTimeWithOffset": "",
              "duration": 230,
              "fareBasis": "",
              "fareType": "PRIVATE",
              "flightNumber": "UO626",
              "flyTime": 0,
              "key": "",
              "mainSegment": true,
              "marriageGrp": "",
              "operatingCarrier": "",
              "operatingFlightNumber": "",
              "seats": 1,
              "status": "",
              "stopCity": [],
              "stopInfo": 0
            }
          ],
          "segmentSplicing": true
        }
      ],
      "itinerarySplicing": false,
      "masterCurrency": "CNY",
      "multiTicket": false,
      "nationalType": 0,
      "nationality": "",
      "onlineCheckIn": false,
      "oriAdultPrice": 97,
      "oriAdultTax": 0,
      "oriChildPrice": 97,
      "oriChildTax": 0,
      "oriInfantPrice": 0,
      "oriInfantTax": 0,
      "policyPriceChanges": [
        {
          "adultChange": {
            "absChange": {
              "amount": 4,
              "currency": "USD"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 0
            },
            "totalChange": {
              "amount": -28,
              "currency": "CNY"
            }
          },
          "childChange": {
            "absChange": {
              "amount": 4,
              "currency": "USD"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 0
            },
            "totalChange": {
              "amount": -28,
              "currency": "CNY"
            }
          },
          "displayNumber": "IC1908021687",
          "infantChange": null,
          "isFeeApplyToProvider": true,
          "otherAbsChangeDetails": [
            {
              "absTotal": {
                "amount": 5,
                "currency": "USD"
              },
              "desc": "INCENTIVE_RECEIVABLE",
              "totalChange": {
                "amount": 35,
                "currency": "CNY"
              }
            }
          ],
          "otherPercentageChangeDetails": [],
          "policyDesc": "IncentivePolicy:IC1908021687",
          "policyId": "5d4411fa73e1340001e3e890",
          "policyType": "INCENTIVE"
        },
        {
          "adultChange": {
            "absChange": {
              "amount": 5,
              "currency": "CNY"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 5.99
            },
            "totalChange": {
              "amount": 52.34449869162856,
              "currency": "CNY"
            }
          },
          "childChange": {
            "absChange": {
              "amount": 5,
              "currency": "CNY"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 5.99
            },
            "totalChange": {
              "amount": 52.34449869162856,
              "currency": "CNY"
            }
          },
          "displayNumber": "PF1907210860",
          "infantChange": {
            "absChange": {
              "amount": 5,
              "currency": "CNY"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 5.99
            },
            "totalChange": {
              "amount": 5.318583129454313,
              "currency": "CNY"
            }
          },
          "isFeeApplyToProvider": true,
          "otherAbsChangeDetails": [],
          "otherPercentageChangeDetails": [],
          "policyDesc": "PlatformPolicy:PF1907210860",
          "policyId": "5d342d9bf24d1c0001195a24",
          "policyType": "PLATFORM"
        }
      ],
      "posLocation": "CN",
      "priceType": 0,
      "providerCurrency": "EUR",
      "providerName": "skypk",
      "providerType": "PROVIDER_API",
      "routingId": "",
      "rule": {
        "changeBeforeDep": 0,
        "changeBeforeDepFee": 0,
        "changeDetail": null,
        "cnRemark": "",
        "currency": "CNY",
        "enRemark": "",
        "manualFareRule": null,
        "miniRule": -404,
        "noShowChange": 0,
        "noShowChangeAfter": 0,
        "noShowChangeAfterFee": 0,
        "noShowChangeFee": 0,
        "noShowRefund": 0,
        "noShowRefundAfter": 0,
        "noShowRefundAfterFee": 0,
        "noShowRefundFee": 0,
        "originRuleFee": {
          "changeAfterFee": -404,
          "changeAfterNoshowFee": -404,
          "changeBeforeFee": -404,
          "changeBeforeNoshowFee": -404,
          "currency": "",
          "refundAfterFee": -404,
          "refundAfterNoshowFee": -404,
          "refundBeforeFee": -404,
          "refundBeforeNoshowFee": -404
        },
        "partEndorse": 0,
        "partEndorsePrice": 0,
        "partRefund": 0,
        "partRefundFee": 0,
        "refundBeforeDep": 0,
        "refundBeforeDepFee": 0,
        "ruleFromOta": -404,
        "useOld": false
      },
      "saleBaggage": false,
      "seats": 1,
      "suitAge": "",
      "ticketInvoiceType": 0,
      "ticketPrice": 0,
      "ticketSource": 0,
      "ticketTimeLimitMinutes": 2880,
      "tof": "",
      "traceSpans": [
        {
          "application": "night-king",
          "createdAt": "2019-08-23T00:51:25.204858737Z",
          "desc": "move amount of 1.000000 from fare price to adult tax",
          "spanId": "2d71957a-bc67-4bd8-a5f6-148357e75e3c",
          "tags": {},
          "traceType": "None"
        },
        {
          "application": "night-king",
          "createdAt": "2019-08-23T00:51:25.204862095Z",
          "desc": "move amount of 1.000000 from child fare price to child tax",
          "spanId": "2eacff16-b0fd-435a-8ed9-4ab293044b1c",
          "tags": {},
          "traceType": "None"
        }
      ],
      "validSegmentsCount": 1,
      "validatingCarrier": "UO",
      "viewPrice": 0
    },
    {
      "accountCode": "",
      "aduTag": "",
      "adultPrice": 789.3922986916286,
      "adultPublishPrice": 766.0478,
      "adultPublishTax": 0,
      "adultTax": 1,
      "adultTaxType": 0,
      "adultType": "",
      "adultUoTax": 0,
      "adultYqTax": 0,
      "adultYrTax": 0,
      "applyType": 0,
      "arf": "",
      "bookingToken": "Aj7BcGvPMW9urK7tcQmdYqtD4Uesb145BQrNTWhy-Q80bbhiIF9MjrHodhyixpRkRr5OOCFy-ddbALMq9Os7juBS-ujhgmbGCjYqL_FiRTYZ5Mbhhy6F1oKltIPvmzcqM7pG8_J50M07NdhjpeCTaE8G11lfOai_uphSEOoCrDl37SlThIhBzBh32JCFxeoNdK4tGufblR6Zrn5K46nhWgnRHwJV3G1irRaf77eDZkuZNU445I35dik9pnP91TSmhv6u1moQeWU_j0BvIEF0OEk7ktDA1OvVBH4LIWbyDSbt_CXFaHYPii-1VyfoNPHoQ7WjPt-RCJ7z1A5b0V-96gXpy2pd_G3msKfiIfGWGZMGD3bGrzbHOeqKuyzRloJ38wFHqpURXTZIU1YCe1SCBBYnYM82xhGgae6ghDYBr1eMKwVCeLK9JW0gnlVHTeXU6",
      "cabin": "E",
      "chiTag": "",
      "childFareBasis": "",
      "childPrice": 789.3922986916286,
      "childPublishPrice": 766.0478,
      "childPublishTax": 0,
      "childTax": 1,
      "childTaxType": 0,
      "childTicketPrice": 0,
      "childType": "",
      "childUoTax": 0,
      "childYqTax": 0,
      "childYrTax": 0,
      "ctof": "",
      "currency": "CNY",
      "currencyConversions": [
        {
          "from": "EUR",
          "rate": 7.8974,
          "source": "BOC",
          "timestamp": "2019-08-23T00:37:25Z",
          "to": "CNY"
        },
        {
          "from": "USD",
          "rate": 7,
          "source": "MANUAL",
          "timestamp": "2019-08-14T07:46:00Z",
          "to": "CNY"
        }
      ],
      "data": "99b6660f-ac71-4a10-8745-dcc9b4cf1e76#f386bd0e-b8fa-4027-a1f9-d07473015b6c#UO618_E",
      "eligibility": "",
      "evictionMarks": [
        {
          "evictionReason": "Platform[去哪人商旅] 航程内拼接",
          "traceSpans": [
            {
              "application": "night-king",
              "createdAt": null,
              "desc": "PlatformConfig filter",
              "spanId": "",
              "tags": {
                "DisplayNumber": "PFC1907306359",
                "Revision": "5"
              },
              "traceType": "None"
            }
          ]
        }
      ],
      "fareBasis": "",
      "fareCalcLine": "",
      "fareType": "PRIVATE",
      "flightCode": "",
      "infantPrice": 0,
      "infantPublishPrice": 0,
      "infantPublishTax": 0,
      "infantTax": 0,
      "infantTaxType": 0,
      "infantType": "",
      "itinerary": [
        {
          "destinationCity": "SEL",
          "duration": 12900,
          "originCity": "HKG",
          "segment": [
            {
              "accountCode": "",
              "aircraftCode": "",
              "arrivalAirport": "ICN",
              "arrivalTerminal": "",
              "arrivalTime": "201909231150",
              "arrivalTimeWithOffset": "",
              "availabilitySource": "",
              "baggage": {
                "baggageCheck": false,
                "freeBaggagePiece": -1,
                "freeBaggageWeight": 0
              },
              "bookingClass": "W",
              "cabin": "E",
              "carrier": "UO",
              "childCabin": "",
              "childFareBasis": "",
              "codeShare": false,
              "connection": false,
              "departureAirport": "HKG",
              "departureTerminal": "",
              "departureTime": "201909230715",
              "departureTimeWithOffset": "",
              "duration": 215,
              "fareBasis": "",
              "fareType": "PRIVATE",
              "flightNumber": "UO618",
              "flyTime": 0,
              "key": "",
              "mainSegment": true,
              "marriageGrp": "",
              "operatingCarrier": "",
              "operatingFlightNumber": "",
              "seats": 1,
              "status": "",
              "stopCity": [],
              "stopInfo": 0
            }
          ],
          "segmentSplicing": true
        }
      ],
      "itinerarySplicing": false,
      "masterCurrency": "CNY",
      "multiTicket": false,
      "nationalType": 0,
      "nationality": "",
      "onlineCheckIn": false,
      "oriAdultPrice": 97,
      "oriAdultTax": 0,
      "oriChildPrice": 97,
      "oriChildTax": 0,
      "oriInfantPrice": 0,
      "oriInfantTax": 0,
      "policyPriceChanges": [
        {
          "adultChange": {
            "absChange": {
              "amount": 4,
              "currency": "USD"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 0
            },
            "totalChange": {
              "amount": -28,
              "currency": "CNY"
            }
          },
          "childChange": {
            "absChange": {
              "amount": 4,
              "currency": "USD"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 0
            },
            "totalChange": {
              "amount": -28,
              "currency": "CNY"
            }
          },
          "displayNumber": "IC1908021687",
          "infantChange": null,
          "isFeeApplyToProvider": true,
          "otherAbsChangeDetails": [
            {
              "absTotal": {
                "amount": 5,
                "currency": "USD"
              },
              "desc": "INCENTIVE_RECEIVABLE",
              "totalChange": {
                "amount": 35,
                "currency": "CNY"
              }
            }
          ],
          "otherPercentageChangeDetails": [],
          "policyDesc": "IncentivePolicy:IC1908021687",
          "policyId": "5d4411fa73e1340001e3e890",
          "policyType": "INCENTIVE"
        },
        {
          "adultChange": {
            "absChange": {
              "amount": 5,
              "currency": "CNY"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 5.99
            },
            "totalChange": {
              "amount": 52.34449869162856,
              "currency": "CNY"
            }
          },
          "childChange": {
            "absChange": {
              "amount": 5,
              "currency": "CNY"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 5.99
            },
            "totalChange": {
              "amount": 52.34449869162856,
              "currency": "CNY"
            }
          },
          "displayNumber": "PF1907210860",
          "infantChange": {
            "absChange": {
              "amount": 5,
              "currency": "CNY"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 5.99
            },
            "totalChange": {
              "amount": 5.318583129454313,
              "currency": "CNY"
            }
          },
          "isFeeApplyToProvider": true,
          "otherAbsChangeDetails": [],
          "otherPercentageChangeDetails": [],
          "policyDesc": "PlatformPolicy:PF1907210860",
          "policyId": "5d342d9bf24d1c0001195a24",
          "policyType": "PLATFORM"
        }
      ],
      "posLocation": "CN",
      "priceType": 0,
      "providerCurrency": "EUR",
      "providerName": "skypk",
      "providerType": "PROVIDER_API",
      "routingId": "",
      "rule": {
        "changeBeforeDep": 0,
        "changeBeforeDepFee": 0,
        "changeDetail": null,
        "cnRemark": "",
        "currency": "CNY",
        "enRemark": "",
        "manualFareRule": null,
        "miniRule": -404,
        "noShowChange": 0,
        "noShowChangeAfter": 0,
        "noShowChangeAfterFee": 0,
        "noShowChangeFee": 0,
        "noShowRefund": 0,
        "noShowRefundAfter": 0,
        "noShowRefundAfterFee": 0,
        "noShowRefundFee": 0,
        "originRuleFee": {
          "changeAfterFee": -404,
          "changeAfterNoshowFee": -404,
          "changeBeforeFee": -404,
          "changeBeforeNoshowFee": -404,
          "currency": "",
          "refundAfterFee": -404,
          "refundAfterNoshowFee": -404,
          "refundBeforeFee": -404,
          "refundBeforeNoshowFee": -404
        },
        "partEndorse": 0,
        "partEndorsePrice": 0,
        "partRefund": 0,
        "partRefundFee": 0,
        "refundBeforeDep": 0,
        "refundBeforeDepFee": 0,
        "ruleFromOta": -404,
        "useOld": false
      },
      "saleBaggage": false,
      "seats": 1,
      "suitAge": "",
      "ticketInvoiceType": 0,
      "ticketPrice": 0,
      "ticketSource": 0,
      "ticketTimeLimitMinutes": 2880,
      "tof": "",
      "traceSpans": [
        {
          "application": "night-king",
          "createdAt": "2019-08-23T00:51:25.204742353Z",
          "desc": "move amount of 1.000000 from fare price to adult tax",
          "spanId": "79ee58c0-d21a-4d6c-a5bf-892201371ac3",
          "tags": {},
          "traceType": "None"
        },
        {
          "application": "night-king",
          "createdAt": "2019-08-23T00:51:25.204745892Z",
          "desc": "move amount of 1.000000 from child fare price to child tax",
          "spanId": "3173f681-ddb1-462a-aa5b-a4a9717dd417",
          "tags": {},
          "traceType": "None"
        }
      ],
      "validSegmentsCount": 1,
      "validatingCarrier": "UO",
      "viewPrice": 0
    },
    {
      "accountCode": "",
      "aduTag": "",
      "adultPrice": 789.3922986916286,
      "adultPublishPrice": 766.0478,
      "adultPublishTax": 0,
      "adultTax": 1,
      "adultTaxType": 0,
      "adultType": "",
      "adultUoTax": 0,
      "adultYqTax": 0,
      "adultYrTax": 0,
      "applyType": 0,
      "arf": "",
      "bookingToken": "A62UQN3Q2Y2CPaKhWpirWphkN7L1f6LkblsgICR1yoF8n2MISo1126FuEJlOT0NA6F1y3rh52yZxSXRJaRXzS8Z1Ib1zKxlgn0t3EABEnsBuKWu-1ftk07hbKYyI7U9xHmJXPTm0JmqIODJ4aC6m5eyiMNTLiR0JcCyLiCxIcO-YISCWJQtjzElrnMObaSIfBaCuAFGggJV9JUOWm_kpG5mS4Tdhjgi0rGSj3uYRNxo8-vDHKmTxykAzY4UN3RzaYvUToi_USbxBp50r9cLWRXpQq15y4fkfJmP8Uq66p11glBx5WJu-nMN_ePB5eDODq1ZP_R3OJG13x1UD0CHCLPp40R75bbJ_JT_c9EZcoiV1yvwk-yOh840_QrKVsItnG-7x24Cwh6ZJaX5W5Jyj5Mxly_68YsmQeQRZwI1PDVMqa8MS_em-jE8j2-wlUaVCg",
      "cabin": "E",
      "chiTag": "",
      "childFareBasis": "",
      "childPrice": 789.3922986916286,
      "childPublishPrice": 766.0478,
      "childPublishTax": 0,
      "childTax": 1,
      "childTaxType": 0,
      "childTicketPrice": 0,
      "childType": "",
      "childUoTax": 0,
      "childYqTax": 0,
      "childYrTax": 0,
      "ctof": "",
      "currency": "CNY",
      "currencyConversions": [
        {
          "from": "EUR",
          "rate": 7.8974,
          "source": "BOC",
          "timestamp": "2019-08-23T00:37:25Z",
          "to": "CNY"
        },
        {
          "from": "USD",
          "rate": 7,
          "source": "MANUAL",
          "timestamp": "2019-08-14T07:46:00Z",
          "to": "CNY"
        }
      ],
      "data": "99b6660f-ac71-4a10-8745-dcc9b4cf1e76#761de634-ad75-4ad1-80a5-8abb0e76256f#UO630_E",
      "eligibility": "",
      "evictionMarks": [
        {
          "evictionReason": "Platform[去哪人商旅] 航程内拼接",
          "traceSpans": [
            {
              "application": "night-king",
              "createdAt": null,
              "desc": "PlatformConfig filter",
              "spanId": "",
              "tags": {
                "DisplayNumber": "PFC1907306359",
                "Revision": "5"
              },
              "traceType": "None"
            }
          ]
        }
      ],
      "fareBasis": "",
      "fareCalcLine": "",
      "fareType": "PRIVATE",
      "flightCode": "",
      "infantPrice": 0,
      "infantPublishPrice": 0,
      "infantPublishTax": 0,
      "infantTax": 0,
      "infantTaxType": 0,
      "infantType": "",
      "itinerary": [
        {
          "destinationCity": "SEL",
          "duration": 13200,
          "originCity": "HKG",
          "segment": [
            {
              "accountCode": "",
              "aircraftCode": "",
              "arrivalAirport": "ICN",
              "arrivalTerminal": "",
              "arrivalTime": "201909231520",
              "arrivalTimeWithOffset": "",
              "availabilitySource": "",
              "baggage": {
                "baggageCheck": false,
                "freeBaggagePiece": -1,
                "freeBaggageWeight": 0
              },
              "bookingClass": "W",
              "cabin": "E",
              "carrier": "UO",
              "childCabin": "",
              "childFareBasis": "",
              "codeShare": false,
              "connection": false,
              "departureAirport": "HKG",
              "departureTerminal": "",
              "departureTime": "201909231040",
              "departureTimeWithOffset": "",
              "duration": 220,
              "fareBasis": "",
              "fareType": "PRIVATE",
              "flightNumber": "UO630",
              "flyTime": 0,
              "key": "",
              "mainSegment": true,
              "marriageGrp": "",
              "operatingCarrier": "UO",
              "operatingFlightNumber": "UO630",
              "seats": 1,
              "status": "",
              "stopCity": [],
              "stopInfo": 0
            }
          ],
          "segmentSplicing": true
        }
      ],
      "itinerarySplicing": false,
      "masterCurrency": "CNY",
      "multiTicket": false,
      "nationalType": 0,
      "nationality": "",
      "onlineCheckIn": false,
      "oriAdultPrice": 97,
      "oriAdultTax": 0,
      "oriChildPrice": 97,
      "oriChildTax": 0,
      "oriInfantPrice": 0,
      "oriInfantTax": 0,
      "policyPriceChanges": [
        {
          "adultChange": {
            "absChange": {
              "amount": 4,
              "currency": "USD"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 0
            },
            "totalChange": {
              "amount": -28,
              "currency": "CNY"
            }
          },
          "childChange": {
            "absChange": {
              "amount": 4,
              "currency": "USD"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 0
            },
            "totalChange": {
              "amount": -28,
              "currency": "CNY"
            }
          },
          "displayNumber": "IC1908021687",
          "infantChange": null,
          "isFeeApplyToProvider": true,
          "otherAbsChangeDetails": [
            {
              "absTotal": {
                "amount": 5,
                "currency": "USD"
              },
              "desc": "INCENTIVE_RECEIVABLE",
              "totalChange": {
                "amount": 35,
                "currency": "CNY"
              }
            }
          ],
          "otherPercentageChangeDetails": [],
          "policyDesc": "IncentivePolicy:IC1908021687",
          "policyId": "5d4411fa73e1340001e3e890",
          "policyType": "INCENTIVE"
        },
        {
          "adultChange": {
            "absChange": {
              "amount": 5,
              "currency": "CNY"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 5.99
            },
            "totalChange": {
              "amount": 52.34449869162856,
              "currency": "CNY"
            }
          },
          "childChange": {
            "absChange": {
              "amount": 5,
              "currency": "CNY"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 5.99
            },
            "totalChange": {
              "amount": 52.34449869162856,
              "currency": "CNY"
            }
          },
          "displayNumber": "PF1907210860",
          "infantChange": {
            "absChange": {
              "amount": 5,
              "currency": "CNY"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 5.99
            },
            "totalChange": {
              "amount": 5.318583129454313,
              "currency": "CNY"
            }
          },
          "isFeeApplyToProvider": true,
          "otherAbsChangeDetails": [],
          "otherPercentageChangeDetails": [],
          "policyDesc": "PlatformPolicy:PF1907210860",
          "policyId": "5d342d9bf24d1c0001195a24",
          "policyType": "PLATFORM"
        }
      ],
      "posLocation": "CN",
      "priceType": 0,
      "providerCurrency": "EUR",
      "providerName": "skypk",
      "providerType": "PROVIDER_API",
      "routingId": "",
      "rule": {
        "changeBeforeDep": 0,
        "changeBeforeDepFee": 0,
        "changeDetail": null,
        "cnRemark": "",
        "currency": "CNY",
        "enRemark": "",
        "manualFareRule": null,
        "miniRule": -404,
        "noShowChange": 0,
        "noShowChangeAfter": 0,
        "noShowChangeAfterFee": 0,
        "noShowChangeFee": 0,
        "noShowRefund": 0,
        "noShowRefundAfter": 0,
        "noShowRefundAfterFee": 0,
        "noShowRefundFee": 0,
        "originRuleFee": {
          "changeAfterFee": -404,
          "changeAfterNoshowFee": -404,
          "changeBeforeFee": -404,
          "changeBeforeNoshowFee": -404,
          "currency": "",
          "refundAfterFee": -404,
          "refundAfterNoshowFee": -404,
          "refundBeforeFee": -404,
          "refundBeforeNoshowFee": -404
        },
        "partEndorse": 0,
        "partEndorsePrice": 0,
        "partRefund": 0,
        "partRefundFee": 0,
        "refundBeforeDep": 0,
        "refundBeforeDepFee": 0,
        "ruleFromOta": -404,
        "useOld": false
      },
      "saleBaggage": false,
      "seats": 1,
      "suitAge": "",
      "ticketInvoiceType": 0,
      "ticketPrice": 0,
      "ticketSource": 0,
      "ticketTimeLimitMinutes": 2880,
      "tof": "",
      "traceSpans": [
        {
          "application": "night-king",
          "createdAt": "2019-08-23T00:51:25.204803028Z",
          "desc": "move amount of 1.000000 from fare price to adult tax",
          "spanId": "58643c6e-63d9-4833-94e7-dc72581a4065",
          "tags": {},
          "traceType": "None"
        },
        {
          "application": "night-king",
          "createdAt": "2019-08-23T00:51:25.204806301Z",
          "desc": "move amount of 1.000000 from child fare price to child tax",
          "spanId": "4ca0592c-d7a4-4de3-8385-544d80782c9d",
          "tags": {},
          "traceType": "None"
        }
      ],
      "validSegmentsCount": 1,
      "validatingCarrier": "UO",
      "viewPrice": 0
    },
    {
      "accountCode": "",
      "aduTag": "",
      "adultPrice": 822.9946814168707,
      "adultPublishPrice": 797.6374000000001,
      "adultPublishTax": 0,
      "adultTax": 1,
      "adultTaxType": 0,
      "adultType": "",
      "adultUoTax": 0,
      "adultYqTax": 0,
      "adultYrTax": 0,
      "applyType": 0,
      "arf": "",
      "bookingToken": "AAVsiUPtb6tgox0qDNh97vUmzWMV71seVztlBzglGoevXQWH3Ib5L1oB4nl1G6wpIAkAcaAztUwQNP5t8V4jLFfI39UWe-DfdRq7d4eljnS5vAkxE3a3I-dglk01JyXANIX9qeWrsUtYSMGs_sNmsm6jXynHyhzDdL-9Gf7mSIt8fRTnIAlsFNkPsu0Ft7Js-6ykMrwCplhxDKNrp9Rpbksv4cFFXTvZN5oFzM7xWnHGaawxnOqDLCxgmDYmetCn44ck56k6HJ0164rutuN8EL-WcM2QbqdBGYKtMPgKtFi9FzBWu60Sln6Kh3-0DpMpqsWvPser1-JniR0wy1TxzC_-D53w3XuOeazu0yn4bg_IhoyByb1rlzfxQsq_CWoFsSZsnBNa6EuN9TsNGj-lyhqsltoBSfUGkZc2sBxcibfrpn_S_uU3TBWrOf_iasEu0",
      "cabin": "E",
      "chiTag": "",
      "childFareBasis": "",
      "childPrice": 822.9946814168707,
      "childPublishPrice": 797.6374000000001,
      "childPublishTax": 0,
      "childTax": 1,
      "childTaxType": 0,
      "childTicketPrice": 0,
      "childType": "",
      "childUoTax": 0,
      "childYqTax": 0,
      "childYrTax": 0,
      "ctof": "",
      "currency": "CNY",
      "currencyConversions": [
        {
          "from": "EUR",
          "rate": 7.8974,
          "source": "BOC",
          "timestamp": "2019-08-23T00:37:25Z",
          "to": "CNY"
        },
        {
          "from": "USD",
          "rate": 7,
          "source": "MANUAL",
          "timestamp": "2019-08-14T07:46:00Z",
          "to": "CNY"
        }
      ],
      "data": "99b6660f-ac71-4a10-8745-dcc9b4cf1e76#2bdf998c-d8f7-497f-a266-bcda8c26c6f2#ZE932_E",
      "eligibility": "",
      "evictionMarks": [
        {
          "evictionReason": "Platform[去哪人商旅] 航程内拼接",
          "traceSpans": [
            {
              "application": "night-king",
              "createdAt": null,
              "desc": "PlatformConfig filter",
              "spanId": "",
              "tags": {
                "DisplayNumber": "PFC1907306359",
                "Revision": "5"
              },
              "traceType": "None"
            }
          ]
        }
      ],
      "fareBasis": "",
      "fareCalcLine": "",
      "fareType": "PRIVATE",
      "flightCode": "",
      "infantPrice": 0,
      "infantPublishPrice": 0,
      "infantPublishTax": 0,
      "infantTax": 0,
      "infantTaxType": 0,
      "infantType": "",
      "itinerary": [
        {
          "destinationCity": "SEL",
          "duration": 13200,
          "originCity": "HKG",
          "segment": [
            {
              "accountCode": "",
              "aircraftCode": "",
              "arrivalAirport": "ICN",
              "arrivalTerminal": "",
              "arrivalTime": "201909231740",
              "arrivalTimeWithOffset": "",
              "availabilitySource": "",
              "baggage": {
                "baggageCheck": false,
                "freeBaggagePiece": -1,
                "freeBaggageWeight": 15
              },
              "bookingClass": "G",
              "cabin": "E",
              "carrier": "ZE",
              "childCabin": "",
              "childFareBasis": "",
              "codeShare": false,
              "connection": false,
              "departureAirport": "HKG",
              "departureTerminal": "",
              "departureTime": "201909231300",
              "departureTimeWithOffset": "",
              "duration": 220,
              "fareBasis": "EOW59",
              "fareType": "PRIVATE",
              "flightNumber": "ZE932",
              "flyTime": 0,
              "key": "",
              "mainSegment": true,
              "marriageGrp": "",
              "operatingCarrier": "",
              "operatingFlightNumber": "",
              "seats": 1,
              "status": "",
              "stopCity": [],
              "stopInfo": 0
            }
          ],
          "segmentSplicing": true
        }
      ],
      "itinerarySplicing": false,
      "masterCurrency": "CNY",
      "multiTicket": false,
      "nationalType": 0,
      "nationality": "",
      "onlineCheckIn": false,
      "oriAdultPrice": 101,
      "oriAdultTax": 0,
      "oriChildPrice": 101,
      "oriChildTax": 0,
      "oriInfantPrice": 0,
      "oriInfantTax": 0,
      "policyPriceChanges": [
        {
          "adultChange": {
            "absChange": {
              "amount": 4,
              "currency": "USD"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 0
            },
            "totalChange": {
              "amount": -28,
              "currency": "CNY"
            }
          },
          "childChange": {
            "absChange": {
              "amount": 4,
              "currency": "USD"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 0
            },
            "totalChange": {
              "amount": -28,
              "currency": "CNY"
            }
          },
          "displayNumber": "IC1908021687",
          "infantChange": null,
          "isFeeApplyToProvider": true,
          "otherAbsChangeDetails": [
            {
              "absTotal": {
                "amount": 5,
                "currency": "USD"
              },
              "desc": "INCENTIVE_RECEIVABLE",
              "totalChange": {
                "amount": 35,
                "currency": "CNY"
              }
            }
          ],
          "otherPercentageChangeDetails": [],
          "policyDesc": "IncentivePolicy:IC1908021687",
          "policyId": "5d4411fa73e1340001e3e890",
          "policyType": "INCENTIVE"
        },
        {
          "adultChange": {
            "absChange": {
              "amount": 5,
              "currency": "CNY"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 5.99
            },
            "totalChange": {
              "amount": 54.35728141687055,
              "currency": "CNY"
            }
          },
          "childChange": {
            "absChange": {
              "amount": 5,
              "currency": "CNY"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 5.99
            },
            "totalChange": {
              "amount": 54.35728141687055,
              "currency": "CNY"
            }
          },
          "displayNumber": "PF1907210860",
          "infantChange": {
            "absChange": {
              "amount": 5,
              "currency": "CNY"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 5.99
            },
            "totalChange": {
              "amount": 5.318583129454313,
              "currency": "CNY"
            }
          },
          "isFeeApplyToProvider": true,
          "otherAbsChangeDetails": [],
          "otherPercentageChangeDetails": [],
          "policyDesc": "PlatformPolicy:PF1907210860",
          "policyId": "5d342d9bf24d1c0001195a24",
          "policyType": "PLATFORM"
        }
      ],
      "posLocation": "CN",
      "priceType": 0,
      "providerCurrency": "EUR",
      "providerName": "skypk",
      "providerType": "PROVIDER_API",
      "routingId": "",
      "rule": {
        "changeBeforeDep": 0,
        "changeBeforeDepFee": 0,
        "changeDetail": null,
        "cnRemark": "",
        "currency": "CNY",
        "enRemark": "",
        "manualFareRule": null,
        "miniRule": 0,
        "noShowChange": 0,
        "noShowChangeAfter": 0,
        "noShowChangeAfterFee": 0,
        "noShowChangeFee": 0,
        "noShowRefund": 0,
        "noShowRefundAfter": 0,
        "noShowRefundAfterFee": 0,
        "noShowRefundFee": 0,
        "originRuleFee": {
          "changeAfterFee": -404,
          "changeAfterNoshowFee": -404,
          "changeBeforeFee": -404,
          "changeBeforeNoshowFee": -404,
          "currency": "",
          "refundAfterFee": -404,
          "refundAfterNoshowFee": -404,
          "refundBeforeFee": -404,
          "refundBeforeNoshowFee": -404
        },
        "partEndorse": 0,
        "partEndorsePrice": 0,
        "partRefund": 0,
        "partRefundFee": 0,
        "refundBeforeDep": 0,
        "refundBeforeDepFee": 0,
        "ruleFromOta": 0,
        "useOld": false
      },
      "saleBaggage": true,
      "seats": 1,
      "suitAge": "",
      "ticketInvoiceType": 0,
      "ticketPrice": 0,
      "ticketSource": 0,
      "ticketTimeLimitMinutes": 2880,
      "tof": "",
      "traceSpans": [
        {
          "application": "night-king",
          "createdAt": "2019-08-23T00:51:25.204914818Z",
          "desc": "move amount of 1.000000 from fare price to adult tax",
          "spanId": "424045e6-7241-456e-8088-2194ff4fec12",
          "tags": {},
          "traceType": "None"
        },
        {
          "application": "night-king",
          "createdAt": "2019-08-23T00:51:25.204918153Z",
          "desc": "move amount of 1.000000 from child fare price to child tax",
          "spanId": "371d832f-d334-4962-b61e-c1e6f600a760",
          "tags": {},
          "traceType": "None"
        }
      ],
      "validSegmentsCount": 1,
      "validatingCarrier": "ZE",
      "viewPrice": 0
    },
    {
      "accountCode": "",
      "aduTag": "",
      "adultPrice": 839.7958727794914,
      "adultPublishPrice": 813.4322,
      "adultPublishTax": 0,
      "adultTax": 1,
      "adultTaxType": 0,
      "adultType": "",
      "adultUoTax": 0,
      "adultYqTax": 0,
      "adultYrTax": 0,
      "applyType": 0,
      "arf": "",
      "bookingToken": "A9OT1GwqXrnKUxI9O5DqSx6PtTWVx48_ZjfWkJnGrdeOSEmkU5HiK3cwGlODl_lk3uxat4YuOQHCBa5kIXa3hqq6HxMkHQ8KsqvB8wpsM5RxtwOyQFZkNgpD4zGCy5dLiVHxS-qoYok4LV_ohi-4tisD2-bTsRtM08rTo09OmMTKXt80SzCmbpcW3eR2KWCugwJ-0QksEHRl5RALuKQzRrTfxuWm2yQThnhlnKDDcrs7Wq2tMBR932GjpCNoJvmPTPjr3vRRBJRvuvwkG0qTm4Vwqhr3Z2TcKstcsAV_uJQcatyn2eU3en6P3PZFFWI6FaOciaVsFZQI7neDuwneGtrtDMozMJFSltPivKBgB0oiLmj34JL_qfAbJ7PA_KOCbg-vpOVLMo6Ju1oCyrFc8bO2llmVV8ePS0SJy3JJt1VOZFsGZUNG6oyvLSkyj_Oh79eaYqyT03oUmCOTxg0gsxg==",
      "cabin": "E",
      "chiTag": "",
      "childFareBasis": "",
      "childPrice": 839.7958727794914,
      "childPublishPrice": 813.4322,
      "childPublishTax": 0,
      "childTax": 1,
      "childTaxType": 0,
      "childTicketPrice": 0,
      "childType": "",
      "childUoTax": 0,
      "childYqTax": 0,
      "childYrTax": 0,
      "ctof": "",
      "currency": "CNY",
      "currencyConversions": [
        {
          "from": "EUR",
          "rate": 7.8974,
          "source": "BOC",
          "timestamp": "2019-08-23T00:37:25Z",
          "to": "CNY"
        },
        {
          "from": "USD",
          "rate": 7,
          "source": "MANUAL",
          "timestamp": "2019-08-14T07:46:00Z",
          "to": "CNY"
        }
      ],
      "data": "99b6660f-ac71-4a10-8745-dcc9b4cf1e76#8fa51dee-94bd-4099-8b91-791df6b12214#LJ114_E",
      "eligibility": "",
      "evictionMarks": [
        {
          "evictionReason": "Platform[去哪人商旅] 航程内拼接",
          "traceSpans": [
            {
              "application": "night-king",
              "createdAt": null,
              "desc": "PlatformConfig filter",
              "spanId": "",
              "tags": {
                "DisplayNumber": "PFC1907306359",
                "Revision": "5"
              },
              "traceType": "None"
            }
          ]
        }
      ],
      "fareBasis": "",
      "fareCalcLine": "",
      "fareType": "PRIVATE",
      "flightCode": "",
      "infantPrice": 0,
      "infantPublishPrice": 0,
      "infantPublishTax": 0,
      "infantTax": 0,
      "infantTaxType": 0,
      "infantType": "",
      "itinerary": [
        {
          "destinationCity": "SEL",
          "duration": 13500,
          "originCity": "HKG",
          "segment": [
            {
              "accountCode": "",
              "aircraftCode": "738",
              "arrivalAirport": "ICN",
              "arrivalTerminal": "",
              "arrivalTime": "201909231805",
              "arrivalTimeWithOffset": "",
              "availabilitySource": "",
              "baggage": {
                "baggageCheck": false,
                "freeBaggagePiece": -1,
                "freeBaggageWeight": 15
              },
              "bookingClass": "S",
              "cabin": "E",
              "carrier": "LJ",
              "childCabin": "",
              "childFareBasis": "",
              "codeShare": false,
              "connection": false,
              "departureAirport": "HKG",
              "departureTerminal": "",
              "departureTime": "201909231320",
              "departureTimeWithOffset": "",
              "duration": 225,
              "fareBasis": "RW1SP",
              "fareType": "PRIVATE",
              "flightNumber": "LJ114",
              "flyTime": 0,
              "key": "",
              "mainSegment": true,
              "marriageGrp": "",
              "operatingCarrier": "LJ",
              "operatingFlightNumber": "LJ114",
              "seats": 1,
              "status": "",
              "stopCity": [],
              "stopInfo": 0
            }
          ],
          "segmentSplicing": true
        }
      ],
      "itinerarySplicing": false,
      "masterCurrency": "CNY",
      "multiTicket": false,
      "nationalType": 0,
      "nationality": "",
      "onlineCheckIn": false,
      "oriAdultPrice": 103,
      "oriAdultTax": 0,
      "oriChildPrice": 103,
      "oriChildTax": 0,
      "oriInfantPrice": 0,
      "oriInfantTax": 0,
      "policyPriceChanges": [
        {
          "adultChange": {
            "absChange": {
              "amount": 4,
              "currency": "USD"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 0
            },
            "totalChange": {
              "amount": -28,
              "currency": "CNY"
            }
          },
          "childChange": {
            "absChange": {
              "amount": 4,
              "currency": "USD"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 0
            },
            "totalChange": {
              "amount": -28,
              "currency": "CNY"
            }
          },
          "displayNumber": "IC1908021687",
          "infantChange": null,
          "isFeeApplyToProvider": true,
          "otherAbsChangeDetails": [
            {
              "absTotal": {
                "amount": 5,
                "currency": "USD"
              },
              "desc": "INCENTIVE_RECEIVABLE",
              "totalChange": {
                "amount": 35,
                "currency": "CNY"
              }
            }
          ],
          "otherPercentageChangeDetails": [],
          "policyDesc": "IncentivePolicy:IC1908021687",
          "policyId": "5d4411fa73e1340001e3e890",
          "policyType": "INCENTIVE"
        },
        {
          "adultChange": {
            "absChange": {
              "amount": 5,
              "currency": "CNY"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 5.99
            },
            "totalChange": {
              "amount": 55.36367277949154,
              "currency": "CNY"
            }
          },
          "childChange": {
            "absChange": {
              "amount": 5,
              "currency": "CNY"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 5.99
            },
            "totalChange": {
              "amount": 55.36367277949154,
              "currency": "CNY"
            }
          },
          "displayNumber": "PF1907210860",
          "infantChange": {
            "absChange": {
              "amount": 5,
              "currency": "CNY"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 5.99
            },
            "totalChange": {
              "amount": 5.318583129454313,
              "currency": "CNY"
            }
          },
          "isFeeApplyToProvider": true,
          "otherAbsChangeDetails": [],
          "otherPercentageChangeDetails": [],
          "policyDesc": "PlatformPolicy:PF1907210860",
          "policyId": "5d342d9bf24d1c0001195a24",
          "policyType": "PLATFORM"
        }
      ],
      "posLocation": "CN",
      "priceType": 0,
      "providerCurrency": "EUR",
      "providerName": "skypk",
      "providerType": "PROVIDER_API",
      "routingId": "",
      "rule": {
        "changeBeforeDep": 0,
        "changeBeforeDepFee": 0,
        "changeDetail": null,
        "cnRemark": "",
        "currency": "CNY",
        "enRemark": "",
        "manualFareRule": null,
        "miniRule": -404,
        "noShowChange": 0,
        "noShowChangeAfter": 0,
        "noShowChangeAfterFee": 0,
        "noShowChangeFee": 0,
        "noShowRefund": 0,
        "noShowRefundAfter": 0,
        "noShowRefundAfterFee": 0,
        "noShowRefundFee": 0,
        "originRuleFee": {
          "changeAfterFee": -404,
          "changeAfterNoshowFee": -404,
          "changeBeforeFee": -404,
          "changeBeforeNoshowFee": -404,
          "currency": "",
          "refundAfterFee": -404,
          "refundAfterNoshowFee": -404,
          "refundBeforeFee": -404,
          "refundBeforeNoshowFee": -404
        },
        "partEndorse": 0,
        "partEndorsePrice": 0,
        "partRefund": 0,
        "partRefundFee": 0,
        "refundBeforeDep": 0,
        "refundBeforeDepFee": 0,
        "ruleFromOta": -404,
        "useOld": false
      },
      "saleBaggage": false,
      "seats": 1,
      "suitAge": "",
      "ticketInvoiceType": 0,
      "ticketPrice": 0,
      "ticketSource": 0,
      "ticketTimeLimitMinutes": 2880,
      "tof": "",
      "traceSpans": [
        {
          "application": "night-king",
          "createdAt": "2019-08-23T00:51:25.204962815Z",
          "desc": "move amount of 1.000000 from fare price to adult tax",
          "spanId": "ef120dd1-fbee-444d-81a6-5f76a2548cf2",
          "tags": {},
          "traceType": "None"
        },
        {
          "application": "night-king",
          "createdAt": "2019-08-23T00:51:25.204966463Z",
          "desc": "move amount of 1.000000 from child fare price to child tax",
          "spanId": "90e5ca15-d810-4496-b7ba-e3423286653a",
          "tags": {},
          "traceType": "None"
        }
      ],
      "validSegmentsCount": 1,
      "validatingCarrier": "LJ",
      "viewPrice": 0
    },
    {
      "accountCode": "",
      "aduTag": "",
      "adultPrice": 1137.635038825657,
      "adultPublishPrice": 1121.4308,
      "adultPublishTax": 0,
      "adultTax": 1,
      "adultTaxType": 0,
      "adultType": "",
      "adultUoTax": 0,
      "adultYqTax": 0,
      "adultYrTax": 0,
      "applyType": 0,
      "arf": "",
      "bookingToken": "ABt3ElzfkRQQw-HvfytnEtYehnkHwMnud8HfKYWGJtcYBJvhU84IFLZlgwG1BVf7Z8fvO3YcN3Qyx7ybVOVxnRtBGnCWAaThDYue0jGoX2xR93A-9PN3j6aSH4c9vZO4ZsJ3Xy2VZdEcsXX_szqet_fJkfjqHcg_fyqDqzfx1zdA0o0cNWOMT1wok_XqRtwCbSVN6QeqsK-cr1C-c7YLAEu4_zx4B6iO8RhTJn_db0yo4MCuPQOfomUQzRVH7uHfaGmOXvlRm89H_UotY6s5QDdgR859pF-MTYvSWMXUhG5KU772XVV3_9Lm8lh15Uy2qj1FRa5xYBeW6sQTH_yVN5Vd6fczX6yeLBAIGaYa2o99UXBy8A64DP6uokANINhRZa0w2tTdEIVXk-Ct_rI77Jn03R9i2GoDvb4CLxxl89rmxNZSqWhfYmXz6wvWILzdn8GD5ho0boF6XM0AJoNFbFC1xhoE6a3xx39unm6TPGrcMUpDDGD4Jm1zk1zX1muq3",
      "cabin": "E",
      "chiTag": "",
      "childFareBasis": "",
      "childPrice": 1137.635038825657,
      "childPublishPrice": 1121.4308,
      "childPublishTax": 0,
      "childTax": 1,
      "childTaxType": 0,
      "childTicketPrice": 0,
      "childType": "",
      "childUoTax": 0,
      "childYqTax": 0,
      "childYrTax": 0,
      "ctof": "",
      "currency": "CNY",
      "currencyConversions": [
        {
          "from": "EUR",
          "rate": 7.8974,
          "source": "BOC",
          "timestamp": "2019-08-23T00:37:25Z",
          "to": "CNY"
        },
        {
          "from": "USD",
          "rate": 7,
          "source": "MANUAL",
          "timestamp": "2019-08-14T07:46:00Z",
          "to": "CNY"
        }
      ],
      "data": "99b6660f-ac71-4a10-8745-dcc9b4cf1e76#66d12c91-8f13-4758-9b27-ffd3ca24a6fe#7C2186_E_ZE202_E",
      "eligibility": "",
      "evictionMarks": [
        {
          "evictionReason": "Platform[去哪人商旅] 航程内拼接",
          "traceSpans": [
            {
              "application": "night-king",
              "createdAt": null,
              "desc": "PlatformConfig filter",
              "spanId": "",
              "tags": {
                "DisplayNumber": "PFC1907306359",
                "Revision": "5"
              },
              "traceType": "None"
            }
          ]
        }
      ],
      "fareBasis": "",
      "fareCalcLine": "",
      "fareType": "PRIVATE",
      "flightCode": "",
      "infantPrice": 0,
      "infantPublishPrice": 0,
      "infantPublishTax": 0,
      "infantTax": 0,
      "infantTaxType": 0,
      "infantType": "",
      "itinerary": [
        {
          "destinationCity": "SEL",
          "duration": 21000,
          "originCity": "HKG",
          "segment": [
            {
              "accountCode": "",
              "aircraftCode": "",
              "arrivalAirport": "CJU",
              "arrivalTerminal": "",
              "arrivalTime": "201909230610",
              "arrivalTimeWithOffset": "",
              "availabilitySource": "",
              "baggage": {
                "baggageCheck": false,
                "freeBaggagePiece": -1,
                "freeBaggageWeight": 0
              },
              "bookingClass": "S",
              "cabin": "E",
              "carrier": "7C",
              "childCabin": "",
              "childFareBasis": "",
              "codeShare": false,
              "connection": false,
              "departureAirport": "HKG",
              "departureTerminal": "",
              "departureTime": "201909230225",
              "departureTimeWithOffset": "",
              "duration": 165,
              "fareBasis": "",
              "fareType": "PRIVATE",
              "flightNumber": "7C2186",
              "flyTime": 0,
              "key": "",
              "mainSegment": true,
              "marriageGrp": "",
              "operatingCarrier": "",
              "operatingFlightNumber": "",
              "seats": 1,
              "status": "",
              "stopCity": [],
              "stopInfo": 0
            },
            {
              "accountCode": "",
              "aircraftCode": "",
              "arrivalAirport": "GMP",
              "arrivalTerminal": "",
              "arrivalTime": "201909230915",
              "arrivalTimeWithOffset": "",
              "availabilitySource": "",
              "baggage": {
                "baggageCheck": true,
                "freeBaggagePiece": -1,
                "freeBaggageWeight": 0
              },
              "bookingClass": "G",
              "cabin": "E",
              "carrier": "ZE",
              "childCabin": "",
              "childFareBasis": "",
              "codeShare": false,
              "connection": false,
              "departureAirport": "CJU",
              "departureTerminal": "",
              "departureTime": "201909230810",
              "departureTimeWithOffset": "",
              "duration": 65,
              "fareBasis": "KNLDC1",
              "fareType": "PRIVATE",
              "flightNumber": "ZE202",
              "flyTime": 0,
              "key": "",
              "mainSegment": false,
              "marriageGrp": "",
              "operatingCarrier": "",
              "operatingFlightNumber": "",
              "seats": 1,
              "status": "",
              "stopCity": [],
              "stopInfo": 0
            }
          ],
          "segmentSplicing": true
        }
      ],
      "itinerarySplicing": false,
      "masterCurrency": "CNY",
      "multiTicket": false,
      "nationalType": 0,
      "nationality": "",
      "onlineCheckIn": false,
      "oriAdultPrice": 142,
      "oriAdultTax": 0,
      "oriChildPrice": 142,
      "oriChildTax": 0,
      "oriInfantPrice": 0,
      "oriInfantTax": 0,
      "policyPriceChanges": [
        {
          "adultChange": {
            "absChange": {
              "amount": 4,
              "currency": "USD"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 0
            },
            "totalChange": {
              "amount": -56,
              "currency": "CNY"
            }
          },
          "childChange": {
            "absChange": {
              "amount": 4,
              "currency": "USD"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 0
            },
            "totalChange": {
              "amount": -56,
              "currency": "CNY"
            }
          },
          "displayNumber": "IC1908021687",
          "infantChange": null,
          "isFeeApplyToProvider": true,
          "otherAbsChangeDetails": [
            {
              "absTotal": {
                "amount": 10,
                "currency": "USD"
              },
              "desc": "INCENTIVE_RECEIVABLE",
              "totalChange": {
                "amount": 70,
                "currency": "CNY"
              }
            }
          ],
          "otherPercentageChangeDetails": [],
          "policyDesc": "IncentivePolicy:IC1908021687",
          "policyId": "5d4411fa73e1340001e3e890",
          "policyType": "INCENTIVE"
        },
        {
          "adultChange": {
            "absChange": {
              "amount": 5,
              "currency": "CNY"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 5.99
            },
            "totalChange": {
              "amount": 73.20423882565684,
              "currency": "CNY"
            }
          },
          "childChange": {
            "absChange": {
              "amount": 5,
              "currency": "CNY"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 5.99
            },
            "totalChange": {
              "amount": 73.20423882565684,
              "currency": "CNY"
            }
          },
          "displayNumber": "PF1907210860",
          "infantChange": {
            "absChange": {
              "amount": 5,
              "currency": "CNY"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 5.99
            },
            "totalChange": {
              "amount": 5.318583129454313,
              "currency": "CNY"
            }
          },
          "isFeeApplyToProvider": true,
          "otherAbsChangeDetails": [],
          "otherPercentageChangeDetails": [],
          "policyDesc": "PlatformPolicy:PF1907210860",
          "policyId": "5d342d9bf24d1c0001195a24",
          "policyType": "PLATFORM"
        }
      ],
      "posLocation": "CN",
      "priceType": 0,
      "providerCurrency": "EUR",
      "providerName": "skypk",
      "providerType": "PROVIDER_API",
      "routingId": "",
      "rule": {
        "changeBeforeDep": 0,
        "changeBeforeDepFee": 0,
        "changeDetail": null,
        "cnRemark": "",
        "currency": "CNY",
        "enRemark": "",
        "manualFareRule": null,
        "miniRule": 0,
        "noShowChange": 0,
        "noShowChangeAfter": 0,
        "noShowChangeAfterFee": 0,
        "noShowChangeFee": 0,
        "noShowRefund": 0,
        "noShowRefundAfter": 0,
        "noShowRefundAfterFee": 0,
        "noShowRefundFee": 0,
        "originRuleFee": {
          "changeAfterFee": -404,
          "changeAfterNoshowFee": -404,
          "changeBeforeFee": -404,
          "changeBeforeNoshowFee": -404,
          "currency": "",
          "refundAfterFee": -404,
          "refundAfterNoshowFee": -404,
          "refundBeforeFee": -404,
          "refundBeforeNoshowFee": -404
        },
        "partEndorse": 0,
        "partEndorsePrice": 0,
        "partRefund": 0,
        "partRefundFee": 0,
        "refundBeforeDep": 0,
        "refundBeforeDepFee": 0,
        "ruleFromOta": 0,
        "useOld": false
      },
      "saleBaggage": true,
      "seats": 1,
      "suitAge": "",
      "ticketInvoiceType": 0,
      "ticketPrice": 0,
      "ticketSource": 0,
      "ticketTimeLimitMinutes": 2880,
      "tof": "",
      "traceSpans": [
        {
          "application": "night-king",
          "createdAt": "2019-08-23T00:51:25.205012072Z",
          "desc": "move amount of 1.000000 from fare price to adult tax",
          "spanId": "4f57f577-3bfd-44c2-8e90-619f104a69da",
          "tags": {},
          "traceType": "None"
        },
        {
          "application": "night-king",
          "createdAt": "2019-08-23T00:51:25.205015975Z",
          "desc": "move amount of 1.000000 from child fare price to child tax",
          "spanId": "333f99fb-eb05-4f8c-b18f-625c0ca369aa",
          "tags": {},
          "traceType": "None"
        }
      ],
      "validSegmentsCount": 2,
      "validatingCarrier": "7C",
      "viewPrice": 0
    },
    {
      "accountCode": "",
      "aduTag": "",
      "adultPrice": 1385.834592064674,
      "adultPublishPrice": 1326.7632,
      "adultPublishTax": 0,
      "adultTax": 1,
      "adultTaxType": 0,
      "adultType": "",
      "adultUoTax": 0,
      "adultYqTax": 0,
      "adultYrTax": 0,
      "applyType": 0,
      "arf": "",
      "bookingToken": "AwXcX8mvxuWzdofDAYFucETZ6mqL3ceoFD4G-UCtyFrEmd4u9N2YS4We7_3tu5zc-LMswFA-00CgsGZK6wejGIvfixsY69aWew0_cDrIVLPsH_Lns--yPov8SEOQpcEyVY5xk-RFluGrYthGhjYnMsV6kptReeynBuIX0PTwSchvGFHq_vR71k_evtiU6xqkGt36XiAI2b6KDcH1TyeB1BDttBbhu2mJbnB48Ycxmfpf1yHu2KvMpF1QZ1RlzQr6ZDNuncqlt0OJuk21qXTFnJI0As0WtOnMxIsvyDtzr9x8lkRGC5oS8Lm7G01gv-D0FfImAQZvC1Eus8lJ2qgtbxTRqf7bNfHip3jzwLrUu6kg7288xL9KMEVx5ijj0yqWJzohA4IpmC5_KtjED04MnTTh9e5eZFZbAvYaEvYBB8I7yAEglA3TJrU_TWccjM_Ca",
      "cabin": "E",
      "chiTag": "",
      "childFareBasis": "",
      "childPrice": 1385.834592064674,
      "childPublishPrice": 1326.7632,
      "childPublishTax": 0,
      "childTax": 1,
      "childTaxType": 0,
      "childTicketPrice": 0,
      "childType": "",
      "childUoTax": 0,
      "childYqTax": 0,
      "childYrTax": 0,
      "ctof": "",
      "currency": "CNY",
      "currencyConversions": [
        {
          "from": "EUR",
          "rate": 7.8974,
          "source": "BOC",
          "timestamp": "2019-08-23T00:37:25Z",
          "to": "CNY"
        },
        {
          "from": "USD",
          "rate": 7,
          "source": "MANUAL",
          "timestamp": "2019-08-14T07:46:00Z",
          "to": "CNY"
        }
      ],
      "data": "99b6660f-ac71-4a10-8745-dcc9b4cf1e76#153fa665-53d5-48f4-8062-7dec13da6b48#HX628_E",
      "eligibility": "",
      "evictionMarks": [
        {
          "evictionReason": "Platform[去哪人商旅] 航程内拼接",
          "traceSpans": [
            {
              "application": "night-king",
              "createdAt": null,
              "desc": "PlatformConfig filter",
              "spanId": "",
              "tags": {
                "DisplayNumber": "PFC1907306359",
                "Revision": "5"
              },
              "traceType": "None"
            }
          ]
        }
      ],
      "fareBasis": "",
      "fareCalcLine": "",
      "fareType": "PRIVATE",
      "flightCode": "",
      "infantPrice": 0,
      "infantPublishPrice": 0,
      "infantPublishTax": 0,
      "infantTax": 0,
      "infantTaxType": 0,
      "infantType": "",
      "itinerary": [
        {
          "destinationCity": "SEL",
          "duration": 13200,
          "originCity": "HKG",
          "segment": [
            {
              "accountCode": "",
              "aircraftCode": "332",
              "arrivalAirport": "ICN",
              "arrivalTerminal": "",
              "arrivalTime": "201909231545",
              "arrivalTimeWithOffset": "",
              "availabilitySource": "",
              "baggage": {
                "baggageCheck": false,
                "freeBaggagePiece": -1,
                "freeBaggageWeight": 20
              },
              "bookingClass": "S",
              "cabin": "E",
              "carrier": "HX",
              "childCabin": "",
              "childFareBasis": "",
              "codeShare": false,
              "connection": false,
              "departureAirport": "HKG",
              "departureTerminal": "",
              "departureTime": "201909231105",
              "departureTimeWithOffset": "",
              "duration": 220,
              "fareBasis": "",
              "fareType": "PRIVATE",
              "flightNumber": "HX628",
              "flyTime": 0,
              "key": "",
              "mainSegment": true,
              "marriageGrp": "",
              "operatingCarrier": "HX",
              "operatingFlightNumber": "HX628",
              "seats": 1,
              "status": "",
              "stopCity": [],
              "stopInfo": 0
            }
          ],
          "segmentSplicing": true
        }
      ],
      "itinerarySplicing": false,
      "masterCurrency": "CNY",
      "multiTicket": false,
      "nationalType": 0,
      "nationality": "",
      "onlineCheckIn": false,
      "oriAdultPrice": 168,
      "oriAdultTax": 0,
      "oriChildPrice": 168,
      "oriChildTax": 0,
      "oriInfantPrice": 0,
      "oriInfantTax": 0,
      "policyPriceChanges": [
        {
          "adultChange": {
            "absChange": {
              "amount": 4,
              "currency": "USD"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 0
            },
            "totalChange": {
              "amount": -28,
              "currency": "CNY"
            }
          },
          "childChange": {
            "absChange": {
              "amount": 4,
              "currency": "USD"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 0
            },
            "totalChange": {
              "amount": -28,
              "currency": "CNY"
            }
          },
          "displayNumber": "IC1908021687",
          "infantChange": null,
          "isFeeApplyToProvider": true,
          "otherAbsChangeDetails": [
            {
              "absTotal": {
                "amount": 5,
                "currency": "USD"
              },
              "desc": "INCENTIVE_RECEIVABLE",
              "totalChange": {
                "amount": 35,
                "currency": "CNY"
              }
            }
          ],
          "otherPercentageChangeDetails": [],
          "policyDesc": "IncentivePolicy:IC1908021687",
          "policyId": "5d4411fa73e1340001e3e890",
          "policyType": "INCENTIVE"
        },
        {
          "adultChange": {
            "absChange": {
              "amount": 5,
              "currency": "CNY"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 5.99
            },
            "totalChange": {
              "amount": 88.07139206467397,
              "currency": "CNY"
            }
          },
          "childChange": {
            "absChange": {
              "amount": 5,
              "currency": "CNY"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 5.99
            },
            "totalChange": {
              "amount": 88.07139206467397,
              "currency": "CNY"
            }
          },
          "displayNumber": "PF1907210860",
          "infantChange": {
            "absChange": {
              "amount": 5,
              "currency": "CNY"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 5.99
            },
            "totalChange": {
              "amount": 5.318583129454313,
              "currency": "CNY"
            }
          },
          "isFeeApplyToProvider": true,
          "otherAbsChangeDetails": [],
          "otherPercentageChangeDetails": [],
          "policyDesc": "PlatformPolicy:PF1907210860",
          "policyId": "5d342d9bf24d1c0001195a24",
          "policyType": "PLATFORM"
        }
      ],
      "posLocation": "CN",
      "priceType": 0,
      "providerCurrency": "EUR",
      "providerName": "skypk",
      "providerType": "PROVIDER_API",
      "routingId": "",
      "rule": {
        "changeBeforeDep": 0,
        "changeBeforeDepFee": 0,
        "changeDetail": null,
        "cnRemark": "",
        "currency": "CNY",
        "enRemark": "",
        "manualFareRule": null,
        "miniRule": -404,
        "noShowChange": 0,
        "noShowChangeAfter": 0,
        "noShowChangeAfterFee": 0,
        "noShowChangeFee": 0,
        "noShowRefund": 0,
        "noShowRefundAfter": 0,
        "noShowRefundAfterFee": 0,
        "noShowRefundFee": 0,
        "originRuleFee": {
          "changeAfterFee": -404,
          "changeAfterNoshowFee": -404,
          "changeBeforeFee": -404,
          "changeBeforeNoshowFee": -404,
          "currency": "",
          "refundAfterFee": -404,
          "refundAfterNoshowFee": -404,
          "refundBeforeFee": -404,
          "refundBeforeNoshowFee": -404
        },
        "partEndorse": 0,
        "partEndorsePrice": 0,
        "partRefund": 0,
        "partRefundFee": 0,
        "refundBeforeDep": 0,
        "refundBeforeDepFee": 0,
        "ruleFromOta": -404,
        "useOld": false
      },
      "saleBaggage": true,
      "seats": 1,
      "suitAge": "",
      "ticketInvoiceType": 0,
      "ticketPrice": 0,
      "ticketSource": 0,
      "ticketTimeLimitMinutes": 2880,
      "tof": "",
      "traceSpans": [
        {
          "application": "night-king",
          "createdAt": "2019-08-23T00:51:25.205059849Z",
          "desc": "move amount of 1.000000 from fare price to adult tax",
          "spanId": "23920eb9-37d0-4dc0-a18a-53d60744db25",
          "tags": {},
          "traceType": "None"
        },
        {
          "application": "night-king",
          "createdAt": "2019-08-23T00:51:25.205062985Z",
          "desc": "move amount of 1.000000 from child fare price to child tax",
          "spanId": "4f06cfa7-1c95-4d92-86ce-0ebb0c64d6a5",
          "tags": {},
          "traceType": "None"
        }
      ],
      "validSegmentsCount": 1,
      "validatingCarrier": "HX",
      "viewPrice": 0
    },
    {
      "accountCode": "",
      "aduTag": "",
      "adultPrice": 1385.834592064674,
      "adultPublishPrice": 1326.7632,
      "adultPublishTax": 0,
      "adultTax": 1,
      "adultTaxType": 0,
      "adultType": "",
      "adultUoTax": 0,
      "adultYqTax": 0,
      "adultYrTax": 0,
      "applyType": 0,
      "arf": "",
      "bookingToken": "A3OStd6fIvdEh2HboYPNRpR7Sz-MCKzAg0vPsABEQkd007cXor7XkKbQ5T4lUXjLcDPgTbHY_QFMWzKVgJNmNE9WPXsny7STPsMGFwcmGVlB8TGveDBa4GbGP92gaaTU-jmegSbtS71AR7wkm77q9Nt-Us7lr7ILFu-SdhLmx9-KjUTqTZN3dYdc2XYUyLX9KdxI3-PSHTfoCvxcZsxuf-YpHGsJBn6kMqLKt38n2J3ywBHpiOpCui-CFmCu2AQlcGGkGc70vzYQHGwlR_xuK3fClKk85Mxbu3gdYi7HCqnQc8OEFSSvE5g_W6SS5GzN3v5YTKEpGpiQ0a8tXAefJwO2BwJe76Wta_2JT-lUZlwGANZWpENw47CbWUvTn_kko_Bv5t1y1Go5VBZ6V-MssNk4qrVZtXvZStBn9Dy4WkEbTAyXut2-Gi3_z1sFzpfJG",
      "cabin": "E",
      "chiTag": "",
      "childFareBasis": "",
      "childPrice": 1385.834592064674,
      "childPublishPrice": 1326.7632,
      "childPublishTax": 0,
      "childTax": 1,
      "childTaxType": 0,
      "childTicketPrice": 0,
      "childType": "",
      "childUoTax": 0,
      "childYqTax": 0,
      "childYrTax": 0,
      "ctof": "",
      "currency": "CNY",
      "currencyConversions": [
        {
          "from": "EUR",
          "rate": 7.8974,
          "source": "BOC",
          "timestamp": "2019-08-23T00:37:25Z",
          "to": "CNY"
        },
        {
          "from": "USD",
          "rate": 7,
          "source": "MANUAL",
          "timestamp": "2019-08-14T07:46:00Z",
          "to": "CNY"
        }
      ],
      "data": "99b6660f-ac71-4a10-8745-dcc9b4cf1e76#ef313602-3494-4837-a515-3b0ac8608aa8#HX646_E",
      "eligibility": "",
      "evictionMarks": [
        {
          "evictionReason": "Platform[去哪人商旅] 航程内拼接",
          "traceSpans": [
            {
              "application": "night-king",
              "createdAt": null,
              "desc": "PlatformConfig filter",
              "spanId": "",
              "tags": {
                "DisplayNumber": "PFC1907306359",
                "Revision": "5"
              },
              "traceType": "None"
            }
          ]
        }
      ],
      "fareBasis": "",
      "fareCalcLine": "",
      "fareType": "PRIVATE",
      "flightCode": "",
      "infantPrice": 0,
      "infantPublishPrice": 0,
      "infantPublishTax": 0,
      "infantTax": 0,
      "infantTaxType": 0,
      "infantType": "",
      "itinerary": [
        {
          "destinationCity": "SEL",
          "duration": 13800,
          "originCity": "HKG",
          "segment": [
            {
              "accountCode": "",
              "aircraftCode": "320",
              "arrivalAirport": "ICN",
              "arrivalTerminal": "",
              "arrivalTime": "201909240425",
              "arrivalTimeWithOffset": "",
              "availabilitySource": "",
              "baggage": {
                "baggageCheck": false,
                "freeBaggagePiece": -1,
                "freeBaggageWeight": 20
              },
              "bookingClass": "S",
              "cabin": "E",
              "carrier": "HX",
              "childCabin": "",
              "childFareBasis": "",
              "codeShare": false,
              "connection": false,
              "departureAirport": "HKG",
              "departureTerminal": "",
              "departureTime": "201909232335",
              "departureTimeWithOffset": "",
              "duration": 230,
              "fareBasis": "",
              "fareType": "PRIVATE",
              "flightNumber": "HX646",
              "flyTime": 0,
              "key": "",
              "mainSegment": true,
              "marriageGrp": "",
              "operatingCarrier": "HX",
              "operatingFlightNumber": "HX646",
              "seats": 1,
              "status": "",
              "stopCity": [],
              "stopInfo": 0
            }
          ],
          "segmentSplicing": true
        }
      ],
      "itinerarySplicing": false,
      "masterCurrency": "CNY",
      "multiTicket": false,
      "nationalType": 0,
      "nationality": "",
      "onlineCheckIn": false,
      "oriAdultPrice": 168,
      "oriAdultTax": 0,
      "oriChildPrice": 168,
      "oriChildTax": 0,
      "oriInfantPrice": 0,
      "oriInfantTax": 0,
      "policyPriceChanges": [
        {
          "adultChange": {
            "absChange": {
              "amount": 4,
              "currency": "USD"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 0
            },
            "totalChange": {
              "amount": -28,
              "currency": "CNY"
            }
          },
          "childChange": {
            "absChange": {
              "amount": 4,
              "currency": "USD"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 0
            },
            "totalChange": {
              "amount": -28,
              "currency": "CNY"
            }
          },
          "displayNumber": "IC1908021687",
          "infantChange": null,
          "isFeeApplyToProvider": true,
          "otherAbsChangeDetails": [
            {
              "absTotal": {
                "amount": 5,
                "currency": "USD"
              },
              "desc": "INCENTIVE_RECEIVABLE",
              "totalChange": {
                "amount": 35,
                "currency": "CNY"
              }
            }
          ],
          "otherPercentageChangeDetails": [],
          "policyDesc": "IncentivePolicy:IC1908021687",
          "policyId": "5d4411fa73e1340001e3e890",
          "policyType": "INCENTIVE"
        },
        {
          "adultChange": {
            "absChange": {
              "amount": 5,
              "currency": "CNY"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 5.99
            },
            "totalChange": {
              "amount": 88.07139206467397,
              "currency": "CNY"
            }
          },
          "childChange": {
            "absChange": {
              "amount": 5,
              "currency": "CNY"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 5.99
            },
            "totalChange": {
              "amount": 88.07139206467397,
              "currency": "CNY"
            }
          },
          "displayNumber": "PF1907210860",
          "infantChange": {
            "absChange": {
              "amount": 5,
              "currency": "CNY"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 5.99
            },
            "totalChange": {
              "amount": 5.318583129454313,
              "currency": "CNY"
            }
          },
          "isFeeApplyToProvider": true,
          "otherAbsChangeDetails": [],
          "otherPercentageChangeDetails": [],
          "policyDesc": "PlatformPolicy:PF1907210860",
          "policyId": "5d342d9bf24d1c0001195a24",
          "policyType": "PLATFORM"
        }
      ],
      "posLocation": "CN",
      "priceType": 0,
      "providerCurrency": "EUR",
      "providerName": "skypk",
      "providerType": "PROVIDER_API",
      "routingId": "",
      "rule": {
        "changeBeforeDep": 0,
        "changeBeforeDepFee": 0,
        "changeDetail": null,
        "cnRemark": "",
        "currency": "CNY",
        "enRemark": "",
        "manualFareRule": null,
        "miniRule": -404,
        "noShowChange": 0,
        "noShowChangeAfter": 0,
        "noShowChangeAfterFee": 0,
        "noShowChangeFee": 0,
        "noShowRefund": 0,
        "noShowRefundAfter": 0,
        "noShowRefundAfterFee": 0,
        "noShowRefundFee": 0,
        "originRuleFee": {
          "changeAfterFee": -404,
          "changeAfterNoshowFee": -404,
          "changeBeforeFee": -404,
          "changeBeforeNoshowFee": -404,
          "currency": "",
          "refundAfterFee": -404,
          "refundAfterNoshowFee": -404,
          "refundBeforeFee": -404,
          "refundBeforeNoshowFee": -404
        },
        "partEndorse": 0,
        "partEndorsePrice": 0,
        "partRefund": 0,
        "partRefundFee": 0,
        "refundBeforeDep": 0,
        "refundBeforeDepFee": 0,
        "ruleFromOta": -404,
        "useOld": false
      },
      "saleBaggage": true,
      "seats": 1,
      "suitAge": "",
      "ticketInvoiceType": 0,
      "ticketPrice": 0,
      "ticketSource": 0,
      "ticketTimeLimitMinutes": 2880,
      "tof": "",
      "traceSpans": [
        {
          "application": "night-king",
          "createdAt": "2019-08-23T00:51:25.205112388Z",
          "desc": "move amount of 1.000000 from fare price to adult tax",
          "spanId": "63df2dd2-3a75-4f46-9c8b-1f2e6c4c45cc",
          "tags": {},
          "traceType": "None"
        },
        {
          "application": "night-king",
          "createdAt": "2019-08-23T00:51:25.205116448Z",
          "desc": "move amount of 1.000000 from child fare price to child tax",
          "spanId": "a3925dd7-e0ee-4770-9f8c-d88b92279c05",
          "tags": {},
          "traceType": "None"
        }
      ],
      "validSegmentsCount": 1,
      "validatingCarrier": "HX",
      "viewPrice": 0
    },
    {
      "accountCode": "",
      "aduTag": "",
      "adultPrice": 1398.0535049462824,
      "adultPublishPrice": 1366.2502,
      "adultPublishTax": 0,
      "adultTax": 1,
      "adultTaxType": 0,
      "adultType": "",
      "adultUoTax": 0,
      "adultYqTax": 0,
      "adultYrTax": 0,
      "applyType": 0,
      "arf": "",
      "bookingToken": "AdhX4Td_2hzFLEBk7pic6ZD814vewmALTIMJUeOaiH6qvcSNF3wLOiKfqYIj-D1f7D6SLERS8sDCIeAaemZ93Dry135bL0aCxxM8QgiTyV__CiY_JUvpbb6KaR_ifuaHzY1i1PLd__31G4hPp36vMmtVx_XHYgmCbHZKATvq29VcnJPiPPoIMxYUqKCxzBiZ1LkcLhyaL7UFiJ-9-OxK1HrAMum_jmblzAPPu7aC42mLcXIPS1XerZy-JiJXHHyY9mHhtuc1pNPrRsXzM95cK34UifuORGwSluA-oeKr1vt-FyIH_S3L0o9BTDP_OgIriaLpJYWYaYu2f0eY5L7iJ2D-52l67prRQ4Ws2X450u5o_CsPqjLj7-trXj4MkiXVZL02C5hqo11k3RPo1hzAQzrMR_hCXm-F3a94nqKzn47Xv1OvaT8G97jJKKxicudRWYjy9a3SvkvZWNehOVsBNRqeQnbIi2Gce1IZ6T2II4CQ=",
      "cabin": "E",
      "chiTag": "",
      "childFareBasis": "",
      "childPrice": 1398.0535049462824,
      "childPublishPrice": 1366.2502,
      "childPublishTax": 0,
      "childTax": 1,
      "childTaxType": 0,
      "childTicketPrice": 0,
      "childType": "",
      "childUoTax": 0,
      "childYqTax": 0,
      "childYrTax": 0,
      "ctof": "",
      "currency": "CNY",
      "currencyConversions": [
        {
          "from": "EUR",
          "rate": 7.8974,
          "source": "BOC",
          "timestamp": "2019-08-23T00:37:25Z",
          "to": "CNY"
        },
        {
          "from": "USD",
          "rate": 7,
          "source": "MANUAL",
          "timestamp": "2019-08-14T07:46:00Z",
          "to": "CNY"
        }
      ],
      "data": "99b6660f-ac71-4a10-8745-dcc9b4cf1e76#522050a6-fff9-4814-845a-3636848e419c#UO686_E_7C1383_E",
      "eligibility": "",
      "evictionMarks": [
        {
          "evictionReason": "Platform[去哪人商旅] 航程内拼接",
          "traceSpans": [
            {
              "application": "night-king",
              "createdAt": null,
              "desc": "PlatformConfig filter",
              "spanId": "",
              "tags": {
                "DisplayNumber": "PFC1907306359",
                "Revision": "5"
              },
              "traceType": "None"
            }
          ]
        }
      ],
      "fareBasis": "",
      "fareCalcLine": "",
      "fareType": "PRIVATE",
      "flightCode": "",
      "infantPrice": 0,
      "infantPublishPrice": 0,
      "infantPublishTax": 0,
      "infantTax": 0,
      "infantTaxType": 0,
      "infantType": "",
      "itinerary": [
        {
          "destinationCity": "SEL",
          "duration": 31200,
          "originCity": "HKG",
          "segment": [
            {
              "accountCode": "",
              "aircraftCode": "",
              "arrivalAirport": "KIX",
              "arrivalTerminal": "",
              "arrivalTime": "201909231340",
              "arrivalTimeWithOffset": "",
              "availabilitySource": "",
              "baggage": {
                "baggageCheck": false,
                "freeBaggagePiece": -1,
                "freeBaggageWeight": 0
              },
              "bookingClass": "W",
              "cabin": "E",
              "carrier": "UO",
              "childCabin": "",
              "childFareBasis": "",
              "codeShare": false,
              "connection": false,
              "departureAirport": "HKG",
              "departureTerminal": "",
              "departureTime": "201909230845",
              "departureTimeWithOffset": "",
              "duration": 235,
              "fareBasis": "",
              "fareType": "PRIVATE",
              "flightNumber": "UO686",
              "flyTime": 0,
              "key": "",
              "mainSegment": true,
              "marriageGrp": "",
              "operatingCarrier": "",
              "operatingFlightNumber": "",
              "seats": 1,
              "status": "",
              "stopCity": [],
              "stopInfo": 0
            },
            {
              "accountCode": "",
              "aircraftCode": "",
              "arrivalAirport": "GMP",
              "arrivalTerminal": "",
              "arrivalTime": "201909231825",
              "arrivalTimeWithOffset": "",
              "availabilitySource": "",
              "baggage": {
                "baggageCheck": true,
                "freeBaggagePiece": -1,
                "freeBaggageWeight": 0
              },
              "bookingClass": "S",
              "cabin": "E",
              "carrier": "7C",
              "childCabin": "",
              "childFareBasis": "",
              "codeShare": false,
              "connection": false,
              "departureAirport": "KIX",
              "departureTerminal": "",
              "departureTime": "201909231630",
              "departureTimeWithOffset": "",
              "duration": 115,
              "fareBasis": "",
              "fareType": "PRIVATE",
              "flightNumber": "7C1383",
              "flyTime": 0,
              "key": "",
              "mainSegment": false,
              "marriageGrp": "",
              "operatingCarrier": "",
              "operatingFlightNumber": "",
              "seats": 1,
              "status": "",
              "stopCity": [],
              "stopInfo": 0
            }
          ],
          "segmentSplicing": true
        }
      ],
      "itinerarySplicing": false,
      "masterCurrency": "CNY",
      "multiTicket": false,
      "nationalType": 0,
      "nationality": "",
      "onlineCheckIn": false,
      "oriAdultPrice": 173,
      "oriAdultTax": 0,
      "oriChildPrice": 173,
      "oriChildTax": 0,
      "oriInfantPrice": 0,
      "oriInfantTax": 0,
      "policyPriceChanges": [
        {
          "adultChange": {
            "absChange": {
              "amount": 4,
              "currency": "USD"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 0
            },
            "totalChange": {
              "amount": -56,
              "currency": "CNY"
            }
          },
          "childChange": {
            "absChange": {
              "amount": 4,
              "currency": "USD"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 0
            },
            "totalChange": {
              "amount": -56,
              "currency": "CNY"
            }
          },
          "displayNumber": "IC1908021687",
          "infantChange": null,
          "isFeeApplyToProvider": true,
          "otherAbsChangeDetails": [
            {
              "absTotal": {
                "amount": 10,
                "currency": "USD"
              },
              "desc": "INCENTIVE_RECEIVABLE",
              "totalChange": {
                "amount": 70,
                "currency": "CNY"
              }
            }
          ],
          "otherPercentageChangeDetails": [],
          "policyDesc": "IncentivePolicy:IC1908021687",
          "policyId": "5d4411fa73e1340001e3e890",
          "policyType": "INCENTIVE"
        },
        {
          "adultChange": {
            "absChange": {
              "amount": 5,
              "currency": "CNY"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 5.99
            },
            "totalChange": {
              "amount": 88.80330494628231,
              "currency": "CNY"
            }
          },
          "childChange": {
            "absChange": {
              "amount": 5,
              "currency": "CNY"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 5.99
            },
            "totalChange": {
              "amount": 88.80330494628231,
              "currency": "CNY"
            }
          },
          "displayNumber": "PF1907210860",
          "infantChange": {
            "absChange": {
              "amount": 5,
              "currency": "CNY"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 5.99
            },
            "totalChange": {
              "amount": 5.318583129454313,
              "currency": "CNY"
            }
          },
          "isFeeApplyToProvider": true,
          "otherAbsChangeDetails": [],
          "otherPercentageChangeDetails": [],
          "policyDesc": "PlatformPolicy:PF1907210860",
          "policyId": "5d342d9bf24d1c0001195a24",
          "policyType": "PLATFORM"
        }
      ],
      "posLocation": "CN",
      "priceType": 0,
      "providerCurrency": "EUR",
      "providerName": "skypk",
      "providerType": "PROVIDER_API",
      "routingId": "",
      "rule": {
        "changeBeforeDep": 0,
        "changeBeforeDepFee": 0,
        "changeDetail": null,
        "cnRemark": "",
        "currency": "CNY",
        "enRemark": "",
        "manualFareRule": null,
        "miniRule": -404,
        "noShowChange": 0,
        "noShowChangeAfter": 0,
        "noShowChangeAfterFee": 0,
        "noShowChangeFee": 0,
        "noShowRefund": 0,
        "noShowRefundAfter": 0,
        "noShowRefundAfterFee": 0,
        "noShowRefundFee": 0,
        "originRuleFee": {
          "changeAfterFee": -404,
          "changeAfterNoshowFee": -404,
          "changeBeforeFee": -404,
          "changeBeforeNoshowFee": -404,
          "currency": "",
          "refundAfterFee": -404,
          "refundAfterNoshowFee": -404,
          "refundBeforeFee": -404,
          "refundBeforeNoshowFee": -404
        },
        "partEndorse": 0,
        "partEndorsePrice": 0,
        "partRefund": 0,
        "partRefundFee": 0,
        "refundBeforeDep": 0,
        "refundBeforeDepFee": 0,
        "ruleFromOta": -404,
        "useOld": false
      },
      "saleBaggage": false,
      "seats": 1,
      "suitAge": "",
      "ticketInvoiceType": 0,
      "ticketPrice": 0,
      "ticketSource": 0,
      "ticketTimeLimitMinutes": 2880,
      "tof": "",
      "traceSpans": [
        {
          "application": "night-king",
          "createdAt": "2019-08-23T00:51:25.205147104Z",
          "desc": "move amount of 1.000000 from fare price to adult tax",
          "spanId": "342a30d4-c91a-4ddf-8113-e8c15c5609b2",
          "tags": {},
          "traceType": "None"
        },
        {
          "application": "night-king",
          "createdAt": "2019-08-23T00:51:25.205150590Z",
          "desc": "move amount of 1.000000 from child fare price to child tax",
          "spanId": "7fbd2494-8303-436d-b9e2-a681f41075da",
          "tags": {},
          "traceType": "None"
        }
      ],
      "validSegmentsCount": 2,
      "validatingCarrier": "UO",
      "viewPrice": 0
    },
    {
      "accountCode": "",
      "aduTag": "",
      "adultPrice": 1695.8926709924476,
      "adultPublishPrice": 1674.2488,
      "adultPublishTax": 0,
      "adultTax": 1,
      "adultTaxType": 0,
      "adultType": "",
      "adultUoTax": 0,
      "adultYqTax": 0,
      "adultYrTax": 0,
      "applyType": 0,
      "arf": "",
      "bookingToken": "A5Av6KzmY4TjR3t9aNR4iZqUReCXQ5R0Vv7EOz_8-Db6-QutMP___ugoZpk7YY3RwY9jbGOdH0dLWUML0ky5oWFtXJyR8Fe5EOblRClIpw8FTc-GtNSuvTMfXb3AvPxRbXa1XLIZMglG9QEX3mYl_qr9plmLg9FBg4hUW3RitZyQXx9u49vYs9Vq8Gujgccn6g-YBX7iAzIHCbIebcYsEqUkbC6i-8mu8JbjMmN-hgkMYeVE-nngywLSmPvWBHDzz7dT4AASwi4tMQkvJsA4hRpQ8abvF2qhLGrFJ0Bq0I-Yi15z2qQQunwV_ChaaUpVnaeawyB2_5SO_EJHtcFZrDT0QUQO18aYCrLUeT2mpb7gZOuadFpppLaC5vloR9dIloiSO8J4STXwRBLIhqkIWwbrI7hUfVFHIEZIkeJub56vipaVRwMT_GyrNQEB-EbAEIps3VagXkH59kwI5I8_rT-YL95sKYxL3JNZyhAZwQic4ICUJOJHn0Dxlwi6OD5ivTo7yVhgTgi-jXHEm41KuUtvEPBu2GzRqlXncUw4qgAU=",
      "cabin": "E",
      "chiTag": "",
      "childFareBasis": "",
      "childPrice": 1695.8926709924476,
      "childPublishPrice": 1674.2488,
      "childPublishTax": 0,
      "childTax": 1,
      "childTaxType": 0,
      "childTicketPrice": 0,
      "childType": "",
      "childUoTax": 0,
      "childYqTax": 0,
      "childYrTax": 0,
      "ctof": "",
      "currency": "CNY",
      "currencyConversions": [
        {
          "from": "EUR",
          "rate": 7.8974,
          "source": "BOC",
          "timestamp": "2019-08-23T00:37:25Z",
          "to": "CNY"
        },
        {
          "from": "USD",
          "rate": 7,
          "source": "MANUAL",
          "timestamp": "2019-08-14T07:46:00Z",
          "to": "CNY"
        }
      ],
      "data": "99b6660f-ac71-4a10-8745-dcc9b4cf1e76#3d247d6c-b792-4102-90f2-6d7029f54037#UO898_E_TW222_E_BX8800_E",
      "eligibility": "",
      "evictionMarks": [
        {
          "evictionReason": "Platform[去哪人商旅] 航程内拼接",
          "traceSpans": [
            {
              "application": "night-king",
              "createdAt": null,
              "desc": "PlatformConfig filter",
              "spanId": "",
              "tags": {
                "DisplayNumber": "PFC1907306359",
                "Revision": "5"
              },
              "traceType": "None"
            }
          ]
        }
      ],
      "fareBasis": "",
      "fareCalcLine": "",
      "fareType": "PRIVATE",
      "flightCode": "",
      "infantPrice": 0,
      "infantPublishPrice": 0,
      "infantPublishTax": 0,
      "infantTax": 0,
      "infantTaxType": 0,
      "infantType": "",
      "itinerary": [
        {
          "destinationCity": "SEL",
          "duration": 70500,
          "originCity": "HKG",
          "segment": [
            {
              "accountCode": "",
              "aircraftCode": "",
              "arrivalAirport": "KIX",
              "arrivalTerminal": "",
              "arrivalTime": "201909231615",
              "arrivalTimeWithOffset": "",
              "availabilitySource": "",
              "baggage": {
                "baggageCheck": false,
                "freeBaggagePiece": -1,
                "freeBaggageWeight": 0
              },
              "bookingClass": "W",
              "cabin": "E",
              "carrier": "UO",
              "childCabin": "",
              "childFareBasis": "",
              "codeShare": false,
              "connection": false,
              "departureAirport": "HKG",
              "departureTerminal": "",
              "departureTime": "201909231120",
              "departureTimeWithOffset": "",
              "duration": 235,
              "fareBasis": "",
              "fareType": "PRIVATE",
              "flightNumber": "UO898",
              "flyTime": 0,
              "key": "",
              "mainSegment": true,
              "marriageGrp": "",
              "operatingCarrier": "",
              "operatingFlightNumber": "",
              "seats": 1,
              "status": "",
              "stopCity": [],
              "stopInfo": 0
            },
            {
              "accountCode": "",
              "aircraftCode": "737",
              "arrivalAirport": "PUS",
              "arrivalTerminal": "",
              "arrivalTime": "201909232135",
              "arrivalTimeWithOffset": "",
              "availabilitySource": "",
              "baggage": {
                "baggageCheck": true,
                "freeBaggagePiece": -1,
                "freeBaggageWeight": 0
              },
              "bookingClass": "S",
              "cabin": "E",
              "carrier": "TW",
              "childCabin": "",
              "childFareBasis": "",
              "codeShare": false,
              "connection": false,
              "departureAirport": "KIX",
              "departureTerminal": "",
              "departureTime": "201909231930",
              "departureTimeWithOffset": "",
              "duration": 125,
              "fareBasis": "IFI",
              "fareType": "PRIVATE",
              "flightNumber": "TW222",
              "flyTime": 0,
              "key": "",
              "mainSegment": false,
              "marriageGrp": "",
              "operatingCarrier": "TW",
              "operatingFlightNumber": "TW222",
              "seats": 1,
              "status": "",
              "stopCity": [],
              "stopInfo": 0
            },
            {
              "accountCode": "",
              "aircraftCode": "",
              "arrivalAirport": "GMP",
              "arrivalTerminal": "",
              "arrivalTime": "201909240755",
              "arrivalTimeWithOffset": "",
              "availabilitySource": "",
              "baggage": {
                "baggageCheck": true,
                "freeBaggagePiece": -1,
                "freeBaggageWeight": 0
              },
              "bookingClass": "G",
              "cabin": "E",
              "carrier": "BX",
              "childCabin": "",
              "childFareBasis": "",
              "codeShare": false,
              "connection": false,
              "departureAirport": "PUS",
              "departureTerminal": "",
              "departureTime": "201909240700",
              "departureTimeWithOffset": "",
              "duration": 55,
              "fareBasis": "",
              "fareType": "PRIVATE",
              "flightNumber": "BX8800",
              "flyTime": 0,
              "key": "",
              "mainSegment": false,
              "marriageGrp": "",
              "operatingCarrier": "",
              "operatingFlightNumber": "",
              "seats": 1,
              "status": "",
              "stopCity": [],
              "stopInfo": 0
            }
          ],
          "segmentSplicing": true
        }
      ],
      "itinerarySplicing": false,
      "masterCurrency": "CNY",
      "multiTicket": false,
      "nationalType": 0,
      "nationality": "",
      "onlineCheckIn": false,
      "oriAdultPrice": 212,
      "oriAdultTax": 0,
      "oriChildPrice": 212,
      "oriChildTax": 0,
      "oriInfantPrice": 0,
      "oriInfantTax": 0,
      "policyPriceChanges": [
        {
          "adultChange": {
            "absChange": {
              "amount": 4,
              "currency": "USD"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 0
            },
            "totalChange": {
              "amount": -84,
              "currency": "CNY"
            }
          },
          "childChange": {
            "absChange": {
              "amount": 4,
              "currency": "USD"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 0
            },
            "totalChange": {
              "amount": -84,
              "currency": "CNY"
            }
          },
          "displayNumber": "IC1908021687",
          "infantChange": null,
          "isFeeApplyToProvider": true,
          "otherAbsChangeDetails": [
            {
              "absTotal": {
                "amount": 15,
                "currency": "USD"
              },
              "desc": "INCENTIVE_RECEIVABLE",
              "totalChange": {
                "amount": 105,
                "currency": "CNY"
              }
            }
          ],
          "otherPercentageChangeDetails": [],
          "policyDesc": "IncentivePolicy:IC1908021687",
          "policyId": "5d4411fa73e1340001e3e890",
          "policyType": "INCENTIVE"
        },
        {
          "adultChange": {
            "absChange": {
              "amount": 5,
              "currency": "CNY"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 5.99
            },
            "totalChange": {
              "amount": 106.6438709924476,
              "currency": "CNY"
            }
          },
          "childChange": {
            "absChange": {
              "amount": 5,
              "currency": "CNY"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 5.99
            },
            "totalChange": {
              "amount": 106.6438709924476,
              "currency": "CNY"
            }
          },
          "displayNumber": "PF1907210860",
          "infantChange": {
            "absChange": {
              "amount": 5,
              "currency": "CNY"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 5.99
            },
            "totalChange": {
              "amount": 5.318583129454313,
              "currency": "CNY"
            }
          },
          "isFeeApplyToProvider": true,
          "otherAbsChangeDetails": [],
          "otherPercentageChangeDetails": [],
          "policyDesc": "PlatformPolicy:PF1907210860",
          "policyId": "5d342d9bf24d1c0001195a24",
          "policyType": "PLATFORM"
        }
      ],
      "posLocation": "CN",
      "priceType": 0,
      "providerCurrency": "EUR",
      "providerName": "skypk",
      "providerType": "PROVIDER_API",
      "routingId": "",
      "rule": {
        "changeBeforeDep": 0,
        "changeBeforeDepFee": 0,
        "changeDetail": null,
        "cnRemark": "",
        "currency": "CNY",
        "enRemark": "",
        "manualFareRule": null,
        "miniRule": -404,
        "noShowChange": 0,
        "noShowChangeAfter": 0,
        "noShowChangeAfterFee": 0,
        "noShowChangeFee": 0,
        "noShowRefund": 0,
        "noShowRefundAfter": 0,
        "noShowRefundAfterFee": 0,
        "noShowRefundFee": 0,
        "originRuleFee": {
          "changeAfterFee": -404,
          "changeAfterNoshowFee": -404,
          "changeBeforeFee": -404,
          "changeBeforeNoshowFee": -404,
          "currency": "",
          "refundAfterFee": -404,
          "refundAfterNoshowFee": -404,
          "refundBeforeFee": -404,
          "refundBeforeNoshowFee": -404
        },
        "partEndorse": 0,
        "partEndorsePrice": 0,
        "partRefund": 0,
        "partRefundFee": 0,
        "refundBeforeDep": 0,
        "refundBeforeDepFee": 0,
        "ruleFromOta": -404,
        "useOld": false
      },
      "saleBaggage": false,
      "seats": 1,
      "suitAge": "",
      "ticketInvoiceType": 0,
      "ticketPrice": 0,
      "ticketSource": 0,
      "ticketTimeLimitMinutes": 2880,
      "tof": "",
      "traceSpans": [
        {
          "application": "night-king",
          "createdAt": "2019-08-23T00:51:25.203659462Z",
          "desc": "move amount of 1.000000 from fare price to adult tax",
          "spanId": "42d36a60-5e55-4d0a-8c65-96e743ebe140",
          "tags": {},
          "traceType": "None"
        },
        {
          "application": "night-king",
          "createdAt": "2019-08-23T00:51:25.203662763Z",
          "desc": "move amount of 1.000000 from child fare price to child tax",
          "spanId": "94c7d125-82c7-4967-9c1b-01f85d029bc7",
          "tags": {},
          "traceType": "None"
        }
      ],
      "validSegmentsCount": 3,
      "validatingCarrier": "UO",
      "viewPrice": 0
    },
    {
      "accountCode": "",
      "aduTag": "",
      "adultPrice": 1805.100414849484,
      "adultPublishPrice": 1776.915,
      "adultPublishTax": 0,
      "adultTax": 1,
      "adultTaxType": 0,
      "adultType": "",
      "adultUoTax": 0,
      "adultYqTax": 0,
      "adultYrTax": 0,
      "applyType": 0,
      "arf": "",
      "bookingToken": "AceRS5aBlbB_c0iXsOMEWNd3LAoZBhk2ejmBtDkXBxczC0Jbuib5v90VSGFKInsgcwa0rGh7eb_3sJpi9RfSyuM3c8k62jJL-pBiJo8zI5rixvUHSfXOgIxIjXD3ZXZw9mlFa-qGu8xO3pUoe1hdr2PQVi_gMhDsjJ8meRisiN09ax6EtuhNKqxaZ7KE_iNvMHJ2GAJukXEsP0ycrrul2T47xkndMTHfrd0VXIpGOuJg1JjosNnyLugH7nTRvTA3JyLmg96YLOPJz955thIJx9eo2WWBJ6-Qy7wGwkejDU5iUBOQdL7o01ASfa2huvLqfoUmNChf3EXxdQ_RLXZBRo9o0ePVhXW90VVE89-fk_ZeHQY0xWOzsjlnK2ESyI5mWUMVvc-twBo7cKqMxWEIejEgWSw53aspWodNoJMLLcqvRCVAXplqt7uLYXiuuISKPW0B302L2KjBLdLGQYIo8Dl8X_n3BlxLw67yVrBXy72ns3UTzzZr7Gg6ld4SiRtRystnc0rX9fjRYUiLYeHL_qRtOW6uExdii3R-UMPEZ7AI=",
      "cabin": "E",
      "chiTag": "",
      "childFareBasis": "",
      "childPrice": 1805.100414849484,
      "childPublishPrice": 1776.915,
      "childPublishTax": 0,
      "childTax": 1,
      "childTaxType": 0,
      "childTicketPrice": 0,
      "childType": "",
      "childUoTax": 0,
      "childYqTax": 0,
      "childYrTax": 0,
      "ctof": "",
      "currency": "CNY",
      "currencyConversions": [
        {
          "from": "EUR",
          "rate": 7.8974,
          "source": "BOC",
          "timestamp": "2019-08-23T00:37:25Z",
          "to": "CNY"
        },
        {
          "from": "USD",
          "rate": 7,
          "source": "MANUAL",
          "timestamp": "2019-08-14T07:46:00Z",
          "to": "CNY"
        }
      ],
      "data": "99b6660f-ac71-4a10-8745-dcc9b4cf1e76#9008955b-ec1c-4e9e-86cf-01a82880d971#UO898_E_LJ218_E_BX8800_E",
      "eligibility": "",
      "evictionMarks": [
        {
          "evictionReason": "Platform[去哪人商旅] 航程内拼接",
          "traceSpans": [
            {
              "application": "night-king",
              "createdAt": null,
              "desc": "PlatformConfig filter",
              "spanId": "",
              "tags": {
                "DisplayNumber": "PFC1907306359",
                "Revision": "5"
              },
              "traceType": "None"
            }
          ]
        }
      ],
      "fareBasis": "",
      "fareCalcLine": "",
      "fareType": "PRIVATE",
      "flightCode": "",
      "infantPrice": 0,
      "infantPublishPrice": 0,
      "infantPublishTax": 0,
      "infantTax": 0,
      "infantTaxType": 0,
      "infantType": "",
      "itinerary": [
        {
          "destinationCity": "SEL",
          "duration": 70500,
          "originCity": "HKG",
          "segment": [
            {
              "accountCode": "",
              "aircraftCode": "",
              "arrivalAirport": "KIX",
              "arrivalTerminal": "",
              "arrivalTime": "201909231615",
              "arrivalTimeWithOffset": "",
              "availabilitySource": "",
              "baggage": {
                "baggageCheck": false,
                "freeBaggagePiece": -1,
                "freeBaggageWeight": 0
              },
              "bookingClass": "W",
              "cabin": "E",
              "carrier": "UO",
              "childCabin": "",
              "childFareBasis": "",
              "codeShare": false,
              "connection": false,
              "departureAirport": "HKG",
              "departureTerminal": "",
              "departureTime": "201909231120",
              "departureTimeWithOffset": "",
              "duration": 235,
              "fareBasis": "",
              "fareType": "PRIVATE",
              "flightNumber": "UO898",
              "flyTime": 0,
              "key": "",
              "mainSegment": true,
              "marriageGrp": "",
              "operatingCarrier": "",
              "operatingFlightNumber": "",
              "seats": 1,
              "status": "",
              "stopCity": [],
              "stopInfo": 0
            },
            {
              "accountCode": "",
              "aircraftCode": "738",
              "arrivalAirport": "PUS",
              "arrivalTerminal": "",
              "arrivalTime": "201909232105",
              "arrivalTimeWithOffset": "",
              "availabilitySource": "",
              "baggage": {
                "baggageCheck": true,
                "freeBaggagePiece": -1,
                "freeBaggageWeight": 0
              },
              "bookingClass": "S",
              "cabin": "E",
              "carrier": "LJ",
              "childCabin": "",
              "childFareBasis": "",
              "codeShare": false,
              "connection": false,
              "departureAirport": "KIX",
              "departureTerminal": "",
              "departureTime": "201909231940",
              "departureTimeWithOffset": "",
              "duration": 85,
              "fareBasis": "I3W1SP",
              "fareType": "PRIVATE",
              "flightNumber": "LJ218",
              "flyTime": 0,
              "key": "",
              "mainSegment": false,
              "marriageGrp": "",
              "operatingCarrier": "LJ",
              "operatingFlightNumber": "LJ218",
              "seats": 1,
              "status": "",
              "stopCity": [],
              "stopInfo": 0
            },
            {
              "accountCode": "",
              "aircraftCode": "",
              "arrivalAirport": "GMP",
              "arrivalTerminal": "",
              "arrivalTime": "201909240755",
              "arrivalTimeWithOffset": "",
              "availabilitySource": "",
              "baggage": {
                "baggageCheck": true,
                "freeBaggagePiece": -1,
                "freeBaggageWeight": 0
              },
              "bookingClass": "G",
              "cabin": "E",
              "carrier": "BX",
              "childCabin": "",
              "childFareBasis": "",
              "codeShare": false,
              "connection": false,
              "departureAirport": "PUS",
              "departureTerminal": "",
              "departureTime": "201909240700",
              "departureTimeWithOffset": "",
              "duration": 55,
              "fareBasis": "",
              "fareType": "PRIVATE",
              "flightNumber": "BX8800",
              "flyTime": 0,
              "key": "",
              "mainSegment": false,
              "marriageGrp": "",
              "operatingCarrier": "",
              "operatingFlightNumber": "",
              "seats": 1,
              "status": "",
              "stopCity": [],
              "stopInfo": 0
            }
          ],
          "segmentSplicing": true
        }
      ],
      "itinerarySplicing": false,
      "masterCurrency": "CNY",
      "multiTicket": false,
      "nationalType": 0,
      "nationality": "",
      "onlineCheckIn": false,
      "oriAdultPrice": 225,
      "oriAdultTax": 0,
      "oriChildPrice": 225,
      "oriChildTax": 0,
      "oriInfantPrice": 0,
      "oriInfantTax": 0,
      "policyPriceChanges": [
        {
          "adultChange": {
            "absChange": {
              "amount": 4,
              "currency": "USD"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 0
            },
            "totalChange": {
              "amount": -84,
              "currency": "CNY"
            }
          },
          "childChange": {
            "absChange": {
              "amount": 4,
              "currency": "USD"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 0
            },
            "totalChange": {
              "amount": -84,
              "currency": "CNY"
            }
          },
          "displayNumber": "IC1908021687",
          "infantChange": null,
          "isFeeApplyToProvider": true,
          "otherAbsChangeDetails": [
            {
              "absTotal": {
                "amount": 15,
                "currency": "USD"
              },
              "desc": "INCENTIVE_RECEIVABLE",
              "totalChange": {
                "amount": 105,
                "currency": "CNY"
              }
            }
          ],
          "otherPercentageChangeDetails": [],
          "policyDesc": "IncentivePolicy:IC1908021687",
          "policyId": "5d4411fa73e1340001e3e890",
          "policyType": "INCENTIVE"
        },
        {
          "adultChange": {
            "absChange": {
              "amount": 5,
              "currency": "CNY"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 5.99
            },
            "totalChange": {
              "amount": 113.18541484948409,
              "currency": "CNY"
            }
          },
          "childChange": {
            "absChange": {
              "amount": 5,
              "currency": "CNY"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 5.99
            },
            "totalChange": {
              "amount": 113.18541484948409,
              "currency": "CNY"
            }
          },
          "displayNumber": "PF1907210860",
          "infantChange": {
            "absChange": {
              "amount": 5,
              "currency": "CNY"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 5.99
            },
            "totalChange": {
              "amount": 5.318583129454313,
              "currency": "CNY"
            }
          },
          "isFeeApplyToProvider": true,
          "otherAbsChangeDetails": [],
          "otherPercentageChangeDetails": [],
          "policyDesc": "PlatformPolicy:PF1907210860",
          "policyId": "5d342d9bf24d1c0001195a24",
          "policyType": "PLATFORM"
        }
      ],
      "posLocation": "CN",
      "priceType": 0,
      "providerCurrency": "EUR",
      "providerName": "skypk",
      "providerType": "PROVIDER_API",
      "routingId": "",
      "rule": {
        "changeBeforeDep": 0,
        "changeBeforeDepFee": 0,
        "changeDetail": null,
        "cnRemark": "",
        "currency": "CNY",
        "enRemark": "",
        "manualFareRule": null,
        "miniRule": -404,
        "noShowChange": 0,
        "noShowChangeAfter": 0,
        "noShowChangeAfterFee": 0,
        "noShowChangeFee": 0,
        "noShowRefund": 0,
        "noShowRefundAfter": 0,
        "noShowRefundAfterFee": 0,
        "noShowRefundFee": 0,
        "originRuleFee": {
          "changeAfterFee": -404,
          "changeAfterNoshowFee": -404,
          "changeBeforeFee": -404,
          "changeBeforeNoshowFee": -404,
          "currency": "",
          "refundAfterFee": -404,
          "refundAfterNoshowFee": -404,
          "refundBeforeFee": -404,
          "refundBeforeNoshowFee": -404
        },
        "partEndorse": 0,
        "partEndorsePrice": 0,
        "partRefund": 0,
        "partRefundFee": 0,
        "refundBeforeDep": 0,
        "refundBeforeDepFee": 0,
        "ruleFromOta": -404,
        "useOld": false
      },
      "saleBaggage": false,
      "seats": 1,
      "suitAge": "",
      "ticketInvoiceType": 0,
      "ticketPrice": 0,
      "ticketSource": 0,
      "ticketTimeLimitMinutes": 2880,
      "tof": "",
      "traceSpans": [
        {
          "application": "night-king",
          "createdAt": "2019-08-23T00:51:25.203073792Z",
          "desc": "move amount of 1.000000 from fare price to adult tax",
          "spanId": "98f2180e-d325-4b85-8b9e-1638dcdd9f27",
          "tags": {},
          "traceType": "None"
        },
        {
          "application": "night-king",
          "createdAt": "2019-08-23T00:51:25.203077841Z",
          "desc": "move amount of 1.000000 from child fare price to child tax",
          "spanId": "19cd722a-433c-4e2a-965a-d0a3a3d6d542",
          "tags": {},
          "traceType": "None"
        }
      ],
      "validSegmentsCount": 3,
      "validatingCarrier": "UO",
      "viewPrice": 0
    },
    {
      "accountCode": "",
      "aduTag": "",
      "adultPrice": 1881.4697372619935,
      "adultPublishPrice": 1792.7098,
      "adultPublishTax": 0,
      "adultTax": 1,
      "adultTaxType": 0,
      "adultType": "",
      "adultUoTax": 0,
      "adultYqTax": 0,
      "adultYrTax": 0,
      "applyType": 0,
      "arf": "",
      "bookingToken": "A-YKTajTmoW0SzondAaoa5e1vV5JtoABGdEzFuHAR_7OzOANRtJBua391Rxy9lAdBWyTxLNxepXrH28Lmz1z5nLNqlR_7noGLYbRfyJewenLqmnYQNIZWfepnNTlgWCeVTf70xIDTYiXTZfsISpsgyjgu6yKJufzRMhoqb_qFFkUdTKBLLwOZdK1UClufdtQgUzUKOUSpaz8YARGe5Lbu7THbooY_S7MK-pbOSATRPd8MSESB8DvelUq0QDH4U7OMvNU5zVLjUXSgflRb3KG3qGZyhHx2PcMBZCBHIzo8HAuOS5a-E9eAfB3vLEHs48h_jL5ZyNSuwlU6QUdmN02lbvRzFzrgtUc34CKmFCJRiwusdvE_pGR-Qc6rtSQ4uCDgZMESYCGfWKsL1nUUNDC7GNTwanzImr2cdMM9bk8aoeIEtLcSxAPr7fgXosxuJpJu6Lq_J5qAdP0sGAoBQtuhzw==",
      "cabin": "E",
      "chiTag": "",
      "childFareBasis": "",
      "childPrice": 1881.4697372619935,
      "childPublishPrice": 1792.7098,
      "childPublishTax": 0,
      "childTax": 1,
      "childTaxType": 0,
      "childTicketPrice": 0,
      "childType": "",
      "childUoTax": 0,
      "childYqTax": 0,
      "childYrTax": 0,
      "ctof": "",
      "currency": "CNY",
      "currencyConversions": [
        {
          "from": "EUR",
          "rate": 7.8974,
          "source": "BOC",
          "timestamp": "2019-08-23T00:37:25Z",
          "to": "CNY"
        },
        {
          "from": "USD",
          "rate": 7,
          "source": "MANUAL",
          "timestamp": "2019-08-14T07:46:00Z",
          "to": "CNY"
        }
      ],
      "data": "99b6660f-ac71-4a10-8745-dcc9b4cf1e76#783ae2da-478c-4de8-a44e-0a01c3e40fc3#KE614_E",
      "eligibility": "",
      "evictionMarks": [
        {
          "evictionReason": "Platform[去哪人商旅] 航程内拼接",
          "traceSpans": [
            {
              "application": "night-king",
              "createdAt": null,
              "desc": "PlatformConfig filter",
              "spanId": "",
              "tags": {
                "DisplayNumber": "PFC1907306359",
                "Revision": "5"
              },
              "traceType": "None"
            }
          ]
        }
      ],
      "fareBasis": "",
      "fareCalcLine": "",
      "fareType": "PRIVATE",
      "flightCode": "",
      "infantPrice": 0,
      "infantPublishPrice": 0,
      "infantPublishTax": 0,
      "infantTax": 0,
      "infantTaxType": 0,
      "infantType": "",
      "itinerary": [
        {
          "destinationCity": "SEL",
          "duration": 13200,
          "originCity": "HKG",
          "segment": [
            {
              "accountCode": "",
              "aircraftCode": "77W",
              "arrivalAirport": "ICN",
              "arrivalTerminal": "",
              "arrivalTime": "201909231845",
              "arrivalTimeWithOffset": "",
              "availabilitySource": "",
              "baggage": {
                "baggageCheck": false,
                "freeBaggagePiece": -1,
                "freeBaggageWeight": 23
              },
              "bookingClass": "N",
              "cabin": "E",
              "carrier": "KE",
              "childCabin": "",
              "childFareBasis": "",
              "codeShare": false,
              "connection": false,
              "departureAirport": "HKG",
              "departureTerminal": "",
              "departureTime": "201909231405",
              "departureTimeWithOffset": "",
              "duration": 220,
              "fareBasis": "ULE00RCK",
              "fareType": "PRIVATE",
              "flightNumber": "KE614",
              "flyTime": 0,
              "key": "",
              "mainSegment": true,
              "marriageGrp": "",
              "operatingCarrier": "KE",
              "operatingFlightNumber": "KE614",
              "seats": 1,
              "status": "",
              "stopCity": [],
              "stopInfo": 0
            }
          ],
          "segmentSplicing": true
        }
      ],
      "itinerarySplicing": false,
      "masterCurrency": "CNY",
      "multiTicket": false,
      "nationalType": 0,
      "nationality": "",
      "onlineCheckIn": true,
      "oriAdultPrice": 227,
      "oriAdultTax": 0,
      "oriChildPrice": 227,
      "oriChildTax": 0,
      "oriInfantPrice": 0,
      "oriInfantTax": 0,
      "policyPriceChanges": [
        {
          "adultChange": {
            "absChange": {
              "amount": 4,
              "currency": "USD"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 0
            },
            "totalChange": {
              "amount": -28,
              "currency": "CNY"
            }
          },
          "childChange": {
            "absChange": {
              "amount": 4,
              "currency": "USD"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 0
            },
            "totalChange": {
              "amount": -28,
              "currency": "CNY"
            }
          },
          "displayNumber": "IC1908021687",
          "infantChange": null,
          "isFeeApplyToProvider": true,
          "otherAbsChangeDetails": [
            {
              "absTotal": {
                "amount": 5,
                "currency": "USD"
              },
              "desc": "INCENTIVE_RECEIVABLE",
              "totalChange": {
                "amount": 35,
                "currency": "CNY"
              }
            }
          ],
          "otherPercentageChangeDetails": [],
          "policyDesc": "IncentivePolicy:IC1908021687",
          "policyId": "5d4411fa73e1340001e3e890",
          "policyType": "INCENTIVE"
        },
        {
          "adultChange": {
            "absChange": {
              "amount": 5,
              "currency": "CNY"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 5.99
            },
            "totalChange": {
              "amount": 117.75993726199341,
              "currency": "CNY"
            }
          },
          "childChange": {
            "absChange": {
              "amount": 5,
              "currency": "CNY"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 5.99
            },
            "totalChange": {
              "amount": 117.75993726199341,
              "currency": "CNY"
            }
          },
          "displayNumber": "PF1907210860",
          "infantChange": {
            "absChange": {
              "amount": 5,
              "currency": "CNY"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 5.99
            },
            "totalChange": {
              "amount": 5.318583129454313,
              "currency": "CNY"
            }
          },
          "isFeeApplyToProvider": true,
          "otherAbsChangeDetails": [],
          "otherPercentageChangeDetails": [],
          "policyDesc": "PlatformPolicy:PF1907210860",
          "policyId": "5d342d9bf24d1c0001195a24",
          "policyType": "PLATFORM"
        }
      ],
      "posLocation": "CN",
      "priceType": 0,
      "providerCurrency": "EUR",
      "providerName": "skypk",
      "providerType": "PROVIDER_API",
      "routingId": "",
      "rule": {
        "changeBeforeDep": 0,
        "changeBeforeDepFee": 0,
        "changeDetail": null,
        "cnRemark": "",
        "currency": "CNY",
        "enRemark": "",
        "manualFareRule": null,
        "miniRule": -404,
        "noShowChange": 0,
        "noShowChangeAfter": 0,
        "noShowChangeAfterFee": 0,
        "noShowChangeFee": 0,
        "noShowRefund": 0,
        "noShowRefundAfter": 0,
        "noShowRefundAfterFee": 0,
        "noShowRefundFee": 0,
        "originRuleFee": {
          "changeAfterFee": -404,
          "changeAfterNoshowFee": -404,
          "changeBeforeFee": -404,
          "changeBeforeNoshowFee": -404,
          "currency": "",
          "refundAfterFee": -404,
          "refundAfterNoshowFee": -404,
          "refundBeforeFee": -404,
          "refundBeforeNoshowFee": -404
        },
        "partEndorse": 0,
        "partEndorsePrice": 0,
        "partRefund": 0,
        "partRefundFee": 0,
        "refundBeforeDep": 0,
        "refundBeforeDepFee": 0,
        "ruleFromOta": -404,
        "useOld": false
      },
      "saleBaggage": false,
      "seats": 1,
      "suitAge": "",
      "ticketInvoiceType": 0,
      "ticketPrice": 0,
      "ticketSource": 0,
      "ticketTimeLimitMinutes": 2880,
      "tof": "",
      "traceSpans": [
        {
          "application": "night-king",
          "createdAt": "2019-08-23T00:51:25.203127089Z",
          "desc": "move amount of 1.000000 from fare price to adult tax",
          "spanId": "b356b3ba-93e6-4bff-b95a-c8949be7fe2b",
          "tags": {},
          "traceType": "None"
        },
        {
          "application": "night-king",
          "createdAt": "2019-08-23T00:51:25.203130818Z",
          "desc": "move amount of 1.000000 from child fare price to child tax",
          "spanId": "4e182e36-dbb1-4ccb-981b-3fad86ef6881",
          "tags": {},
          "traceType": "None"
        }
      ],
      "validSegmentsCount": 1,
      "validatingCarrier": "KE",
      "viewPrice": 0
    },
    {
      "accountCode": "",
      "aduTag": "",
      "adultPrice": 1881.4697372619935,
      "adultPublishPrice": 1792.7098,
      "adultPublishTax": 0,
      "adultTax": 1,
      "adultTaxType": 0,
      "adultType": "",
      "adultUoTax": 0,
      "adultYqTax": 0,
      "adultYrTax": 0,
      "applyType": 0,
      "arf": "",
      "bookingToken": "AM3eeeCKYZ_5IkingmBWdZeb3xJZPIhnNysoKgISKtAojrGrcio-B_p0HejPJj_T7Wm5oGDth14qpXcBYEk2Sjg2kSKqRw86GWY27mNywqWQc9CGAABDGy-JxntJGdEgBYVn33OmXPBopbKdqUsUpCScDO2iLpYl4qiILcN53idW0CBVvpfYZF1G16d6HxgTNFhQtW2tvXCzXHKbCu_zsxeXtqkj0Me-Lj-VjAzyYPacl0fnHequyV1YeLBpOGC_4WecgHRA7Pb3vq2RTLiL8wXhvVZWZJcJO3iuHvUmQVY41dzA5Qvv4VJrA-Ohxtv4qo4JiSmgJqcPL4y3N0OMbE8UA5GbPr8lgxltWodLzga4WuEfjwiKNFUNhuZZXuUHdk-9lp3Q5o7ke-QA92uyoGoJIadFsacS8mfboui1TwXEk_ZZ8mrRcp4IEwDxETyWYKu5hkYRW24uRh4XV5deETA==",
      "cabin": "E",
      "chiTag": "",
      "childFareBasis": "",
      "childPrice": 1881.4697372619935,
      "childPublishPrice": 1792.7098,
      "childPublishTax": 0,
      "childTax": 1,
      "childTaxType": 0,
      "childTicketPrice": 0,
      "childType": "",
      "childUoTax": 0,
      "childYqTax": 0,
      "childYrTax": 0,
      "ctof": "",
      "currency": "CNY",
      "currencyConversions": [
        {
          "from": "EUR",
          "rate": 7.8974,
          "source": "BOC",
          "timestamp": "2019-08-23T00:37:25Z",
          "to": "CNY"
        },
        {
          "from": "USD",
          "rate": 7,
          "source": "MANUAL",
          "timestamp": "2019-08-14T07:46:00Z",
          "to": "CNY"
        }
      ],
      "data": "99b6660f-ac71-4a10-8745-dcc9b4cf1e76#b977b58b-023f-4e55-93ef-3681aec6d2dc#KE608_E",
      "eligibility": "",
      "evictionMarks": [
        {
          "evictionReason": "Platform[去哪人商旅] 航程内拼接",
          "traceSpans": [
            {
              "application": "night-king",
              "createdAt": null,
              "desc": "PlatformConfig filter",
              "spanId": "",
              "tags": {
                "DisplayNumber": "PFC1907306359",
                "Revision": "5"
              },
              "traceType": "None"
            }
          ]
        }
      ],
      "fareBasis": "",
      "fareCalcLine": "",
      "fareType": "PRIVATE",
      "flightCode": "",
      "infantPrice": 0,
      "infantPublishPrice": 0,
      "infantPublishTax": 0,
      "infantTax": 0,
      "infantTaxType": 0,
      "infantType": "",
      "itinerary": [
        {
          "destinationCity": "SEL",
          "duration": 13200,
          "originCity": "HKG",
          "segment": [
            {
              "accountCode": "",
              "aircraftCode": "789",
              "arrivalAirport": "ICN",
              "arrivalTerminal": "",
              "arrivalTime": "201909230525",
              "arrivalTimeWithOffset": "",
              "availabilitySource": "",
              "baggage": {
                "baggageCheck": false,
                "freeBaggagePiece": -1,
                "freeBaggageWeight": 23
              },
              "bookingClass": "N",
              "cabin": "E",
              "carrier": "KE",
              "childCabin": "",
              "childFareBasis": "",
              "codeShare": false,
              "connection": false,
              "departureAirport": "HKG",
              "departureTerminal": "",
              "departureTime": "201909230045",
              "departureTimeWithOffset": "",
              "duration": 220,
              "fareBasis": "ULE00RCK",
              "fareType": "PRIVATE",
              "flightNumber": "KE608",
              "flyTime": 0,
              "key": "",
              "mainSegment": true,
              "marriageGrp": "",
              "operatingCarrier": "KE",
              "operatingFlightNumber": "KE608",
              "seats": 1,
              "status": "",
              "stopCity": [],
              "stopInfo": 0
            }
          ],
          "segmentSplicing": true
        }
      ],
      "itinerarySplicing": false,
      "masterCurrency": "CNY",
      "multiTicket": false,
      "nationalType": 0,
      "nationality": "",
      "onlineCheckIn": true,
      "oriAdultPrice": 227,
      "oriAdultTax": 0,
      "oriChildPrice": 227,
      "oriChildTax": 0,
      "oriInfantPrice": 0,
      "oriInfantTax": 0,
      "policyPriceChanges": [
        {
          "adultChange": {
            "absChange": {
              "amount": 4,
              "currency": "USD"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 0
            },
            "totalChange": {
              "amount": -28,
              "currency": "CNY"
            }
          },
          "childChange": {
            "absChange": {
              "amount": 4,
              "currency": "USD"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 0
            },
            "totalChange": {
              "amount": -28,
              "currency": "CNY"
            }
          },
          "displayNumber": "IC1908021687",
          "infantChange": null,
          "isFeeApplyToProvider": true,
          "otherAbsChangeDetails": [
            {
              "absTotal": {
                "amount": 5,
                "currency": "USD"
              },
              "desc": "INCENTIVE_RECEIVABLE",
              "totalChange": {
                "amount": 35,
                "currency": "CNY"
              }
            }
          ],
          "otherPercentageChangeDetails": [],
          "policyDesc": "IncentivePolicy:IC1908021687",
          "policyId": "5d4411fa73e1340001e3e890",
          "policyType": "INCENTIVE"
        },
        {
          "adultChange": {
            "absChange": {
              "amount": 5,
              "currency": "CNY"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 5.99
            },
            "totalChange": {
              "amount": 117.75993726199341,
              "currency": "CNY"
            }
          },
          "childChange": {
            "absChange": {
              "amount": 5,
              "currency": "CNY"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 5.99
            },
            "totalChange": {
              "amount": 117.75993726199341,
              "currency": "CNY"
            }
          },
          "displayNumber": "PF1907210860",
          "infantChange": {
            "absChange": {
              "amount": 5,
              "currency": "CNY"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 5.99
            },
            "totalChange": {
              "amount": 5.318583129454313,
              "currency": "CNY"
            }
          },
          "isFeeApplyToProvider": true,
          "otherAbsChangeDetails": [],
          "otherPercentageChangeDetails": [],
          "policyDesc": "PlatformPolicy:PF1907210860",
          "policyId": "5d342d9bf24d1c0001195a24",
          "policyType": "PLATFORM"
        }
      ],
      "posLocation": "CN",
      "priceType": 0,
      "providerCurrency": "EUR",
      "providerName": "skypk",
      "providerType": "PROVIDER_API",
      "routingId": "",
      "rule": {
        "changeBeforeDep": 0,
        "changeBeforeDepFee": 0,
        "changeDetail": null,
        "cnRemark": "",
        "currency": "CNY",
        "enRemark": "",
        "manualFareRule": null,
        "miniRule": -404,
        "noShowChange": 0,
        "noShowChangeAfter": 0,
        "noShowChangeAfterFee": 0,
        "noShowChangeFee": 0,
        "noShowRefund": 0,
        "noShowRefundAfter": 0,
        "noShowRefundAfterFee": 0,
        "noShowRefundFee": 0,
        "originRuleFee": {
          "changeAfterFee": -404,
          "changeAfterNoshowFee": -404,
          "changeBeforeFee": -404,
          "changeBeforeNoshowFee": -404,
          "currency": "",
          "refundAfterFee": -404,
          "refundAfterNoshowFee": -404,
          "refundBeforeFee": -404,
          "refundBeforeNoshowFee": -404
        },
        "partEndorse": 0,
        "partEndorsePrice": 0,
        "partRefund": 0,
        "partRefundFee": 0,
        "refundBeforeDep": 0,
        "refundBeforeDepFee": 0,
        "ruleFromOta": -404,
        "useOld": false
      },
      "saleBaggage": false,
      "seats": 1,
      "suitAge": "",
      "ticketInvoiceType": 0,
      "ticketPrice": 0,
      "ticketSource": 0,
      "ticketTimeLimitMinutes": 2880,
      "tof": "",
      "traceSpans": [
        {
          "application": "night-king",
          "createdAt": "2019-08-23T00:51:25.203176848Z",
          "desc": "move amount of 1.000000 from fare price to adult tax",
          "spanId": "b3efcded-10c9-462e-937d-0b00f0f57b6b",
          "tags": {},
          "traceType": "None"
        },
        {
          "application": "night-king",
          "createdAt": "2019-08-23T00:51:25.203180152Z",
          "desc": "move amount of 1.000000 from child fare price to child tax",
          "spanId": "cc4bc655-962f-4e37-886a-2d92637d3174",
          "tags": {},
          "traceType": "None"
        }
      ],
      "validSegmentsCount": 1,
      "validatingCarrier": "KE",
      "viewPrice": 0
    },
    {
      "accountCode": "",
      "aduTag": "",
      "adultPrice": 1881.4697372619935,
      "adultPublishPrice": 1792.7098,
      "adultPublishTax": 0,
      "adultTax": 1,
      "adultTaxType": 0,
      "adultType": "",
      "adultUoTax": 0,
      "adultYqTax": 0,
      "adultYrTax": 0,
      "applyType": 0,
      "arf": "",
      "bookingToken": "ADGSwfV6k7gPiNp-i3MvC7UHsxe5cceTggeYfFkzAt88lJzq-GsqkRKD2A_S86smolDIs0c3L4LlvWxHdYjUXVEfBWjxivoL9GVHRCom80Mwz0O1mTeBMMBUE-Avohv2YAvG8sKMZmQjmKuQK2DL1Z8xXCs3lYrlE23SksxAbF8la1xcVgT8mmmHWK6PA03Rk-d3XB_tf74C-5il0t11vZv-F2zVdn-NFoI9oqBoOAEvi4bzcD560IJy2KjywO8rfezOeQxI750uQdYUvF99grJnZetTkT178LERLej1WhmHrs3H4khtjLFeJguqgd9lpzgtECrqWzN_6flOlA-IRq-Qd5z13YAc236pJjmtlIE-mA_RGWUhQx5h-fv_zmsx1LGVxUoCFygdak8biLcdcUa8Joyodp1WN0Y3YpGa7DlmYvLMJLeZgmu_PV3Bj8aWAHlHKsaWzU5dOV_DqQ_eobQ==",
      "cabin": "E",
      "chiTag": "",
      "childFareBasis": "",
      "childPrice": 1881.4697372619935,
      "childPublishPrice": 1792.7098,
      "childPublishTax": 0,
      "childTax": 1,
      "childTaxType": 0,
      "childTicketPrice": 0,
      "childType": "",
      "childUoTax": 0,
      "childYqTax": 0,
      "childYrTax": 0,
      "ctof": "",
      "currency": "CNY",
      "currencyConversions": [
        {
          "from": "EUR",
          "rate": 7.8974,
          "source": "BOC",
          "timestamp": "2019-08-23T00:37:25Z",
          "to": "CNY"
        },
        {
          "from": "USD",
          "rate": 7,
          "source": "MANUAL",
          "timestamp": "2019-08-14T07:46:00Z",
          "to": "CNY"
        }
      ],
      "data": "99b6660f-ac71-4a10-8745-dcc9b4cf1e76#fad0ebad-f045-43b1-b460-61638a8b4919#KE602_E",
      "eligibility": "",
      "evictionMarks": [
        {
          "evictionReason": "Platform[去哪人商旅] 航程内拼接",
          "traceSpans": [
            {
              "application": "night-king",
              "createdAt": null,
              "desc": "PlatformConfig filter",
              "spanId": "",
              "tags": {
                "DisplayNumber": "PFC1907306359",
                "Revision": "5"
              },
              "traceType": "None"
            }
          ]
        }
      ],
      "fareBasis": "",
      "fareCalcLine": "",
      "fareType": "PRIVATE",
      "flightCode": "",
      "infantPrice": 0,
      "infantPublishPrice": 0,
      "infantPublishTax": 0,
      "infantTax": 0,
      "infantTaxType": 0,
      "infantType": "",
      "itinerary": [
        {
          "destinationCity": "SEL",
          "duration": 13200,
          "originCity": "HKG",
          "segment": [
            {
              "accountCode": "",
              "aircraftCode": "74H",
              "arrivalAirport": "ICN",
              "arrivalTerminal": "",
              "arrivalTime": "201909232235",
              "arrivalTimeWithOffset": "",
              "availabilitySource": "",
              "baggage": {
                "baggageCheck": false,
                "freeBaggagePiece": -1,
                "freeBaggageWeight": 23
              },
              "bookingClass": "N",
              "cabin": "E",
              "carrier": "KE",
              "childCabin": "",
              "childFareBasis": "",
              "codeShare": false,
              "connection": false,
              "departureAirport": "HKG",
              "departureTerminal": "",
              "departureTime": "201909231755",
              "departureTimeWithOffset": "",
              "duration": 220,
              "fareBasis": "ULE00RCK",
              "fareType": "PRIVATE",
              "flightNumber": "KE602",
              "flyTime": 0,
              "key": "",
              "mainSegment": true,
              "marriageGrp": "",
              "operatingCarrier": "KE",
              "operatingFlightNumber": "KE602",
              "seats": 1,
              "status": "",
              "stopCity": [],
              "stopInfo": 0
            }
          ],
          "segmentSplicing": true
        }
      ],
      "itinerarySplicing": false,
      "masterCurrency": "CNY",
      "multiTicket": false,
      "nationalType": 0,
      "nationality": "",
      "onlineCheckIn": true,
      "oriAdultPrice": 227,
      "oriAdultTax": 0,
      "oriChildPrice": 227,
      "oriChildTax": 0,
      "oriInfantPrice": 0,
      "oriInfantTax": 0,
      "policyPriceChanges": [
        {
          "adultChange": {
            "absChange": {
              "amount": 4,
              "currency": "USD"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 0
            },
            "totalChange": {
              "amount": -28,
              "currency": "CNY"
            }
          },
          "childChange": {
            "absChange": {
              "amount": 4,
              "currency": "USD"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 0
            },
            "totalChange": {
              "amount": -28,
              "currency": "CNY"
            }
          },
          "displayNumber": "IC1908021687",
          "infantChange": null,
          "isFeeApplyToProvider": true,
          "otherAbsChangeDetails": [
            {
              "absTotal": {
                "amount": 5,
                "currency": "USD"
              },
              "desc": "INCENTIVE_RECEIVABLE",
              "totalChange": {
                "amount": 35,
                "currency": "CNY"
              }
            }
          ],
          "otherPercentageChangeDetails": [],
          "policyDesc": "IncentivePolicy:IC1908021687",
          "policyId": "5d4411fa73e1340001e3e890",
          "policyType": "INCENTIVE"
        },
        {
          "adultChange": {
            "absChange": {
              "amount": 5,
              "currency": "CNY"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 5.99
            },
            "totalChange": {
              "amount": 117.75993726199341,
              "currency": "CNY"
            }
          },
          "childChange": {
            "absChange": {
              "amount": 5,
              "currency": "CNY"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 5.99
            },
            "totalChange": {
              "amount": 117.75993726199341,
              "currency": "CNY"
            }
          },
          "displayNumber": "PF1907210860",
          "infantChange": {
            "absChange": {
              "amount": 5,
              "currency": "CNY"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 5.99
            },
            "totalChange": {
              "amount": 5.318583129454313,
              "currency": "CNY"
            }
          },
          "isFeeApplyToProvider": true,
          "otherAbsChangeDetails": [],
          "otherPercentageChangeDetails": [],
          "policyDesc": "PlatformPolicy:PF1907210860",
          "policyId": "5d342d9bf24d1c0001195a24",
          "policyType": "PLATFORM"
        }
      ],
      "posLocation": "CN",
      "priceType": 0,
      "providerCurrency": "EUR",
      "providerName": "skypk",
      "providerType": "PROVIDER_API",
      "routingId": "",
      "rule": {
        "changeBeforeDep": 0,
        "changeBeforeDepFee": 0,
        "changeDetail": null,
        "cnRemark": "",
        "currency": "CNY",
        "enRemark": "",
        "manualFareRule": null,
        "miniRule": -404,
        "noShowChange": 0,
        "noShowChangeAfter": 0,
        "noShowChangeAfterFee": 0,
        "noShowChangeFee": 0,
        "noShowRefund": 0,
        "noShowRefundAfter": 0,
        "noShowRefundAfterFee": 0,
        "noShowRefundFee": 0,
        "originRuleFee": {
          "changeAfterFee": -404,
          "changeAfterNoshowFee": -404,
          "changeBeforeFee": -404,
          "changeBeforeNoshowFee": -404,
          "currency": "",
          "refundAfterFee": -404,
          "refundAfterNoshowFee": -404,
          "refundBeforeFee": -404,
          "refundBeforeNoshowFee": -404
        },
        "partEndorse": 0,
        "partEndorsePrice": 0,
        "partRefund": 0,
        "partRefundFee": 0,
        "refundBeforeDep": 0,
        "refundBeforeDepFee": 0,
        "ruleFromOta": -404,
        "useOld": false
      },
      "saleBaggage": false,
      "seats": 1,
      "suitAge": "",
      "ticketInvoiceType": 0,
      "ticketPrice": 0,
      "ticketSource": 0,
      "ticketTimeLimitMinutes": 2880,
      "tof": "",
      "traceSpans": [
        {
          "application": "night-king",
          "createdAt": "2019-08-23T00:51:25.203224628Z",
          "desc": "move amount of 1.000000 from fare price to adult tax",
          "spanId": "1de4c00b-1187-4efd-a3fc-7f826ddfe1f8",
          "tags": {},
          "traceType": "None"
        },
        {
          "application": "night-king",
          "createdAt": "2019-08-23T00:51:25.203228972Z",
          "desc": "move amount of 1.000000 from child fare price to child tax",
          "spanId": "82f8ef61-8a29-42bc-b476-67be36bb5aa0",
          "tags": {},
          "traceType": "None"
        }
      ],
      "validSegmentsCount": 1,
      "validatingCarrier": "KE",
      "viewPrice": 0
    },
    {
      "accountCode": "",
      "aduTag": "",
      "adultPrice": 1881.4697372619935,
      "adultPublishPrice": 1792.7098,
      "adultPublishTax": 0,
      "adultTax": 1,
      "adultTaxType": 0,
      "adultType": "",
      "adultUoTax": 0,
      "adultYqTax": 0,
      "adultYrTax": 0,
      "applyType": 0,
      "arf": "",
      "bookingToken": "ADGSwfV6k7gPiNp-i3MvC7UHsxe5cceTggeYfFkzAt8_RtNyB6t9hLgOaAZhxWdIvPXmL_bwuilumm3MSFx7hQQlf_QSMeNCPl0l3rRkxsRszTVVicWXQ1RZhf6gMJeRtahJ1TMzUZjzFImTdrbgyAzlxo-00lGx0_WkmIiS54Ye41qHx3XlDAzsbM9zV-8bhs2Ho6oRDHFwT8dyuRlIGa8HF1YQkrOOIoQ5wpdp8WoGt4MdjgqGjel2zAO_ZURnyUeIBKt66dswrze0qrhTKbHiVnQKiLHyQudrHbU0WO3WBBGchF-SNZXTJRkVhi_4BxbXsGazSreekNC0Lap_0dkSp7hxb1736ost7P0hUU5ujVQ2faQVwTWa7yh1f8292vMGaeSuN-cokJiFCDx0pJ3vcj3yPiMZBTImI7yoNFdULBAyTpZLv29S2iRzvKjUGZIm50O09wG0Z0prwhpS2jw==",
      "cabin": "E",
      "chiTag": "",
      "childFareBasis": "",
      "childPrice": 1881.4697372619935,
      "childPublishPrice": 1792.7098,
      "childPublishTax": 0,
      "childTax": 1,
      "childTaxType": 0,
      "childTicketPrice": 0,
      "childType": "",
      "childUoTax": 0,
      "childYqTax": 0,
      "childYrTax": 0,
      "ctof": "",
      "currency": "CNY",
      "currencyConversions": [
        {
          "from": "EUR",
          "rate": 7.8974,
          "source": "BOC",
          "timestamp": "2019-08-23T00:37:25Z",
          "to": "CNY"
        },
        {
          "from": "USD",
          "rate": 7,
          "source": "MANUAL",
          "timestamp": "2019-08-14T07:46:00Z",
          "to": "CNY"
        }
      ],
      "data": "99b6660f-ac71-4a10-8745-dcc9b4cf1e76#47fb602b-3726-4815-9c14-386199dd129a#KE604_E",
      "eligibility": "",
      "evictionMarks": [
        {
          "evictionReason": "Platform[去哪人商旅] 航程内拼接",
          "traceSpans": [
            {
              "application": "night-king",
              "createdAt": null,
              "desc": "PlatformConfig filter",
              "spanId": "",
              "tags": {
                "DisplayNumber": "PFC1907306359",
                "Revision": "5"
              },
              "traceType": "None"
            }
          ]
        }
      ],
      "fareBasis": "",
      "fareCalcLine": "",
      "fareType": "PRIVATE",
      "flightCode": "",
      "infantPrice": 0,
      "infantPublishPrice": 0,
      "infantPublishTax": 0,
      "infantTax": 0,
      "infantTaxType": 0,
      "infantType": "",
      "itinerary": [
        {
          "destinationCity": "SEL",
          "duration": 13500,
          "originCity": "HKG",
          "segment": [
            {
              "accountCode": "",
              "aircraftCode": "789",
              "arrivalAirport": "ICN",
              "arrivalTerminal": "",
              "arrivalTime": "201909231700",
              "arrivalTimeWithOffset": "",
              "availabilitySource": "",
              "baggage": {
                "baggageCheck": false,
                "freeBaggagePiece": -1,
                "freeBaggageWeight": 23
              },
              "bookingClass": "N",
              "cabin": "E",
              "carrier": "KE",
              "childCabin": "",
              "childFareBasis": "",
              "codeShare": false,
              "connection": false,
              "departureAirport": "HKG",
              "departureTerminal": "",
              "departureTime": "201909231215",
              "departureTimeWithOffset": "",
              "duration": 225,
              "fareBasis": "ULE00RCK",
              "fareType": "PRIVATE",
              "flightNumber": "KE604",
              "flyTime": 0,
              "key": "",
              "mainSegment": true,
              "marriageGrp": "",
              "operatingCarrier": "KE",
              "operatingFlightNumber": "KE604",
              "seats": 1,
              "status": "",
              "stopCity": [],
              "stopInfo": 0
            }
          ],
          "segmentSplicing": true
        }
      ],
      "itinerarySplicing": false,
      "masterCurrency": "CNY",
      "multiTicket": false,
      "nationalType": 0,
      "nationality": "",
      "onlineCheckIn": true,
      "oriAdultPrice": 227,
      "oriAdultTax": 0,
      "oriChildPrice": 227,
      "oriChildTax": 0,
      "oriInfantPrice": 0,
      "oriInfantTax": 0,
      "policyPriceChanges": [
        {
          "adultChange": {
            "absChange": {
              "amount": 4,
              "currency": "USD"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 0
            },
            "totalChange": {
              "amount": -28,
              "currency": "CNY"
            }
          },
          "childChange": {
            "absChange": {
              "amount": 4,
              "currency": "USD"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 0
            },
            "totalChange": {
              "amount": -28,
              "currency": "CNY"
            }
          },
          "displayNumber": "IC1908021687",
          "infantChange": null,
          "isFeeApplyToProvider": true,
          "otherAbsChangeDetails": [
            {
              "absTotal": {
                "amount": 5,
                "currency": "USD"
              },
              "desc": "INCENTIVE_RECEIVABLE",
              "totalChange": {
                "amount": 35,
                "currency": "CNY"
              }
            }
          ],
          "otherPercentageChangeDetails": [],
          "policyDesc": "IncentivePolicy:IC1908021687",
          "policyId": "5d4411fa73e1340001e3e890",
          "policyType": "INCENTIVE"
        },
        {
          "adultChange": {
            "absChange": {
              "amount": 5,
              "currency": "CNY"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 5.99
            },
            "totalChange": {
              "amount": 117.75993726199341,
              "currency": "CNY"
            }
          },
          "childChange": {
            "absChange": {
              "amount": 5,
              "currency": "CNY"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 5.99
            },
            "totalChange": {
              "amount": 117.75993726199341,
              "currency": "CNY"
            }
          },
          "displayNumber": "PF1907210860",
          "infantChange": {
            "absChange": {
              "amount": 5,
              "currency": "CNY"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 5.99
            },
            "totalChange": {
              "amount": 5.318583129454313,
              "currency": "CNY"
            }
          },
          "isFeeApplyToProvider": true,
          "otherAbsChangeDetails": [],
          "otherPercentageChangeDetails": [],
          "policyDesc": "PlatformPolicy:PF1907210860",
          "policyId": "5d342d9bf24d1c0001195a24",
          "policyType": "PLATFORM"
        }
      ],
      "posLocation": "CN",
      "priceType": 0,
      "providerCurrency": "EUR",
      "providerName": "skypk",
      "providerType": "PROVIDER_API",
      "routingId": "",
      "rule": {
        "changeBeforeDep": 0,
        "changeBeforeDepFee": 0,
        "changeDetail": null,
        "cnRemark": "",
        "currency": "CNY",
        "enRemark": "",
        "manualFareRule": null,
        "miniRule": -404,
        "noShowChange": 0,
        "noShowChangeAfter": 0,
        "noShowChangeAfterFee": 0,
        "noShowChangeFee": 0,
        "noShowRefund": 0,
        "noShowRefundAfter": 0,
        "noShowRefundAfterFee": 0,
        "noShowRefundFee": 0,
        "originRuleFee": {
          "changeAfterFee": -404,
          "changeAfterNoshowFee": -404,
          "changeBeforeFee": -404,
          "changeBeforeNoshowFee": -404,
          "currency": "",
          "refundAfterFee": -404,
          "refundAfterNoshowFee": -404,
          "refundBeforeFee": -404,
          "refundBeforeNoshowFee": -404
        },
        "partEndorse": 0,
        "partEndorsePrice": 0,
        "partRefund": 0,
        "partRefundFee": 0,
        "refundBeforeDep": 0,
        "refundBeforeDepFee": 0,
        "ruleFromOta": -404,
        "useOld": false
      },
      "saleBaggage": false,
      "seats": 1,
      "suitAge": "",
      "ticketInvoiceType": 0,
      "ticketPrice": 0,
      "ticketSource": 0,
      "ticketTimeLimitMinutes": 2880,
      "tof": "",
      "traceSpans": [
        {
          "application": "night-king",
          "createdAt": "2019-08-23T00:51:25.203279173Z",
          "desc": "move amount of 1.000000 from fare price to adult tax",
          "spanId": "5a4339ee-e3a4-4d28-ba68-88d432528150",
          "tags": {},
          "traceType": "None"
        },
        {
          "application": "night-king",
          "createdAt": "2019-08-23T00:51:25.203282405Z",
          "desc": "move amount of 1.000000 from child fare price to child tax",
          "spanId": "46d5be2e-b53c-4f1e-bff7-c634a9c31b14",
          "tags": {},
          "traceType": "None"
        }
      ],
      "validSegmentsCount": 1,
      "validatingCarrier": "KE",
      "viewPrice": 0
    },
    {
      "accountCode": "",
      "aduTag": "",
      "adultPrice": 1994.4957983193276,
      "adultPublishPrice": 1926.9656,
      "adultPublishTax": 0,
      "adultTax": 1,
      "adultTaxType": 0,
      "adultType": "",
      "adultUoTax": 0,
      "adultYqTax": 0,
      "adultYrTax": 0,
      "applyType": 0,
      "arf": "",
      "bookingToken": "AOl0VO4F1ze4LAnAPbaRXWNotqJFNV_papKLPrqR5geF3M-DMB40E02P3ky_QYnQwuYmC8uvYr_h1IpJwf5JBSbsnMeZ897j_Cy6mhZTva1MgO_owa7ajmLBgyNXiQpHEsy3GpCYaiW7TT3GEMj3fHRSGyZ77iwC2yzBpfQ-Xe12H9Nal8YVrMP2lbN8Xqt6S4jPqsJlpqgyjDNqBg0SZ2XVuR_E584ssR-mA6ABXx661Ig3bP64HzJ86AggOmFIzipAq7mh1Q0LAzKP006kMaxTRBSLvPwWXTufgR1BXoYmwxjEfGyml7CgZfn2HKBkkb3jVfYIAAoDVKEUc1YlJmUM3K_wWJi_MsTg98wWlZ0QTF1ASfkDC7-0yxpXoruocxg2YIxZTvXALIH7WUljcVqMgwuoNC2IKUE4duDacY-bUiCe6d-ikUI4odXXLCRLxCL38Bi2pfo9EKqTBJO8W2w8pdgvdMbEgqHaIl1G6NQs=",
      "cabin": "E",
      "chiTag": "",
      "childFareBasis": "",
      "childPrice": 1994.4957983193276,
      "childPublishPrice": 1926.9656,
      "childPublishTax": 0,
      "childTax": 1,
      "childTaxType": 0,
      "childTicketPrice": 0,
      "childType": "",
      "childUoTax": 0,
      "childYqTax": 0,
      "childYrTax": 0,
      "ctof": "",
      "currency": "CNY",
      "currencyConversions": [
        {
          "from": "EUR",
          "rate": 7.8974,
          "source": "BOC",
          "timestamp": "2019-08-23T00:37:25Z",
          "to": "CNY"
        },
        {
          "from": "USD",
          "rate": 7,
          "source": "MANUAL",
          "timestamp": "2019-08-14T07:46:00Z",
          "to": "CNY"
        }
      ],
      "data": "99b6660f-ac71-4a10-8745-dcc9b4cf1e76#590b4d9c-d460-407f-b82d-d794a72de509#CA112_E_CA137_E",
      "eligibility": "",
      "evictionMarks": [
        {
          "evictionReason": "Platform[去哪人商旅] 最小中转时间",
          "traceSpans": [
            {
              "application": "night-king",
              "createdAt": null,
              "desc": "PlatformConfig filter",
              "spanId": "",
              "tags": {
                "DisplayNumber": "PFC1907306359",
                "Revision": "5"
              },
              "traceType": "None"
            }
          ]
        },
        {
          "evictionReason": "Platform[去哪人商旅] 航程内拼接",
          "traceSpans": [
            {
              "application": "night-king",
              "createdAt": null,
              "desc": "PlatformConfig filter",
              "spanId": "",
              "tags": {
                "DisplayNumber": "PFC1907306359",
                "Revision": "5"
              },
              "traceType": "None"
            }
          ]
        }
      ],
      "fareBasis": "",
      "fareCalcLine": "",
      "fareType": "PRIVATE",
      "flightCode": "",
      "infantPrice": 0,
      "infantPublishPrice": 0,
      "infantPublishTax": 0,
      "infantTax": 0,
      "infantTaxType": 0,
      "infantType": "",
      "itinerary": [
        {
          "destinationCity": "SEL",
          "duration": 24000,
          "originCity": "HKG",
          "segment": [
            {
              "accountCode": "",
              "aircraftCode": "738",
              "arrivalAirport": "PEK",
              "arrivalTerminal": "",
              "arrivalTime": "201909231730",
              "arrivalTimeWithOffset": "",
              "availabilitySource": "",
              "baggage": {
                "baggageCheck": false,
                "freeBaggagePiece": -1,
                "freeBaggageWeight": 20
              },
              "bookingClass": "S",
              "cabin": "E",
              "carrier": "CA",
              "childCabin": "",
              "childFareBasis": "",
              "codeShare": false,
              "connection": false,
              "departureAirport": "HKG",
              "departureTerminal": "",
              "departureTime": "201909231410",
              "departureTimeWithOffset": "",
              "duration": 200,
              "fareBasis": "WLORFHK6",
              "fareType": "PRIVATE",
              "flightNumber": "CA112",
              "flyTime": 0,
              "key": "",
              "mainSegment": true,
              "marriageGrp": "",
              "operatingCarrier": "CA",
              "operatingFlightNumber": "CA112",
              "seats": 1,
              "status": "",
              "stopCity": [],
              "stopInfo": 0
            },
            {
              "accountCode": "",
              "aircraftCode": "738",
              "arrivalAirport": "GMP",
              "arrivalTerminal": "",
              "arrivalTime": "201909232150",
              "arrivalTimeWithOffset": "",
              "availabilitySource": "",
              "baggage": {
                "baggageCheck": false,
                "freeBaggagePiece": -1,
                "freeBaggageWeight": 20
              },
              "bookingClass": "S",
              "cabin": "E",
              "carrier": "CA",
              "childCabin": "",
              "childFareBasis": "",
              "codeShare": false,
              "connection": false,
              "departureAirport": "PEK",
              "departureTerminal": "",
              "departureTime": "201909231845",
              "departureTimeWithOffset": "",
              "duration": 125,
              "fareBasis": "WLORFHK6",
              "fareType": "PRIVATE",
              "flightNumber": "CA137",
              "flyTime": 0,
              "key": "",
              "mainSegment": false,
              "marriageGrp": "",
              "operatingCarrier": "CA",
              "operatingFlightNumber": "CA137",
              "seats": 1,
              "status": "",
              "stopCity": [],
              "stopInfo": 0
            }
          ],
          "segmentSplicing": true
        }
      ],
      "itinerarySplicing": false,
      "masterCurrency": "CNY",
      "multiTicket": false,
      "nationalType": 0,
      "nationality": "",
      "onlineCheckIn": false,
      "oriAdultPrice": 244,
      "oriAdultTax": 0,
      "oriChildPrice": 244,
      "oriChildTax": 0,
      "oriInfantPrice": 0,
      "oriInfantTax": 0,
      "policyPriceChanges": [
        {
          "adultChange": {
            "absChange": {
              "amount": 4,
              "currency": "USD"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 0
            },
            "totalChange": {
              "amount": -56,
              "currency": "CNY"
            }
          },
          "childChange": {
            "absChange": {
              "amount": 4,
              "currency": "USD"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 0
            },
            "totalChange": {
              "amount": -56,
              "currency": "CNY"
            }
          },
          "displayNumber": "IC1908021687",
          "infantChange": null,
          "isFeeApplyToProvider": true,
          "otherAbsChangeDetails": [
            {
              "absTotal": {
                "amount": 10,
                "currency": "USD"
              },
              "desc": "INCENTIVE_RECEIVABLE",
              "totalChange": {
                "amount": 70,
                "currency": "CNY"
              }
            }
          ],
          "otherPercentageChangeDetails": [],
          "policyDesc": "IncentivePolicy:IC1908021687",
          "policyId": "5d4411fa73e1340001e3e890",
          "policyType": "INCENTIVE"
        },
        {
          "adultChange": {
            "absChange": {
              "amount": 5,
              "currency": "CNY"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 5.99
            },
            "totalChange": {
              "amount": 124.53019831932772,
              "currency": "CNY"
            }
          },
          "childChange": {
            "absChange": {
              "amount": 5,
              "currency": "CNY"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 5.99
            },
            "totalChange": {
              "amount": 124.53019831932772,
              "currency": "CNY"
            }
          },
          "displayNumber": "PF1907210860",
          "infantChange": {
            "absChange": {
              "amount": 5,
              "currency": "CNY"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 5.99
            },
            "totalChange": {
              "amount": 5.318583129454313,
              "currency": "CNY"
            }
          },
          "isFeeApplyToProvider": true,
          "otherAbsChangeDetails": [],
          "otherPercentageChangeDetails": [],
          "policyDesc": "PlatformPolicy:PF1907210860",
          "policyId": "5d342d9bf24d1c0001195a24",
          "policyType": "PLATFORM"
        }
      ],
      "posLocation": "CN",
      "priceType": 0,
      "providerCurrency": "EUR",
      "providerName": "skypk",
      "providerType": "PROVIDER_API",
      "routingId": "",
      "rule": {
        "changeBeforeDep": 0,
        "changeBeforeDepFee": 0,
        "changeDetail": null,
        "cnRemark": "",
        "currency": "CNY",
        "enRemark": "",
        "manualFareRule": null,
        "miniRule": -404,
        "noShowChange": 0,
        "noShowChangeAfter": 0,
        "noShowChangeAfterFee": 0,
        "noShowChangeFee": 0,
        "noShowRefund": 0,
        "noShowRefundAfter": 0,
        "noShowRefundAfterFee": 0,
        "noShowRefundFee": 0,
        "originRuleFee": {
          "changeAfterFee": -404,
          "changeAfterNoshowFee": -404,
          "changeBeforeFee": -404,
          "changeBeforeNoshowFee": -404,
          "currency": "",
          "refundAfterFee": -404,
          "refundAfterNoshowFee": -404,
          "refundBeforeFee": -404,
          "refundBeforeNoshowFee": -404
        },
        "partEndorse": 0,
        "partEndorsePrice": 0,
        "partRefund": 0,
        "partRefundFee": 0,
        "refundBeforeDep": 0,
        "refundBeforeDepFee": 0,
        "ruleFromOta": -404,
        "useOld": false
      },
      "saleBaggage": false,
      "seats": 1,
      "suitAge": "",
      "ticketInvoiceType": 0,
      "ticketPrice": 0,
      "ticketSource": 0,
      "ticketTimeLimitMinutes": 2880,
      "tof": "",
      "traceSpans": [
        {
          "application": "night-king",
          "createdAt": "2019-08-23T00:51:25.203727843Z",
          "desc": "move amount of 1.000000 from fare price to adult tax",
          "spanId": "dc08fd09-d346-4de0-8c1f-532eed33848d",
          "tags": {},
          "traceType": "None"
        },
        {
          "application": "night-king",
          "createdAt": "2019-08-23T00:51:25.203731161Z",
          "desc": "move amount of 1.000000 from child fare price to child tax",
          "spanId": "e1f0c41d-6756-4df6-a927-59c2239788f6",
          "tags": {},
          "traceType": "None"
        }
      ],
      "validSegmentsCount": 2,
      "validatingCarrier": "CA",
      "viewPrice": 0
    },
    {
      "accountCode": "",
      "aduTag": "",
      "adultPrice": 1994.4957983193276,
      "adultPublishPrice": 1926.9656,
      "adultPublishTax": 0,
      "adultTax": 1,
      "adultTaxType": 0,
      "adultType": "",
      "adultUoTax": 0,
      "adultYqTax": 0,
      "adultYrTax": 0,
      "applyType": 0,
      "arf": "",
      "bookingToken": "ASLxozeZZm4EZlmrUGIqsIlpdx_Mac4fARvdSmvpiqVl0u52SiQD64xR9vrr1V_J24zC-CFpvuYVVgZUW7GXmfyBG5w47P8ssQB4DYgEOy_tFCw4ca9iuX6DKO-dfQAOJEeje3ihMj6k1eo5RYPif80RKS_6RYRPNyBMeU7LDWdGOjdbhvWasHpHOtSRazYN3F2Eol10ODOZOITAu4xv6oXLU26gtkVGRlSBiNjY_A-ta2ELH511zvqtK5oYgpa6mTJHqFTkKhFrgzGzBA-cnERvRXJqcE9bgPglSsEy4hGyW0UILqmvfeu9Fdkxq8DXpbLFjbjF2rcRkv_vK-tSb74UrIgUBsgq0gNZ__iKjhHHr-5PeUWZTvBsqS9YN8RCgFiXib7rKD7xMym2kHy0JamxvodKmFPiT2c7W9v1T360lhqsmKYMVjVtN1h5xPNvYXg5QgfPSlvdxpGdmxGf-0ryp5ZoT-QJFt8Mlwj0Ly0s=",
      "cabin": "E",
      "chiTag": "",
      "childFareBasis": "",
      "childPrice": 1994.4957983193276,
      "childPublishPrice": 1926.9656,
      "childPublishTax": 0,
      "childTax": 1,
      "childTaxType": 0,
      "childTicketPrice": 0,
      "childType": "",
      "childUoTax": 0,
      "childYqTax": 0,
      "childYrTax": 0,
      "ctof": "",
      "currency": "CNY",
      "currencyConversions": [
        {
          "from": "EUR",
          "rate": 7.8974,
          "source": "BOC",
          "timestamp": "2019-08-23T00:37:25Z",
          "to": "CNY"
        },
        {
          "from": "USD",
          "rate": 7,
          "source": "MANUAL",
          "timestamp": "2019-08-14T07:46:00Z",
          "to": "CNY"
        }
      ],
      "data": "99b6660f-ac71-4a10-8745-dcc9b4cf1e76#6692e423-57ae-428c-bb98-645efccff2e2#CA102_E_CA137_E",
      "eligibility": "",
      "evictionMarks": [
        {
          "evictionReason": "Platform[去哪人商旅] 航程内拼接",
          "traceSpans": [
            {
              "application": "night-king",
              "createdAt": null,
              "desc": "PlatformConfig filter",
              "spanId": "",
              "tags": {
                "DisplayNumber": "PFC1907306359",
                "Revision": "5"
              },
              "traceType": "None"
            }
          ]
        }
      ],
      "fareBasis": "",
      "fareCalcLine": "",
      "fareType": "PRIVATE",
      "flightCode": "",
      "infantPrice": 0,
      "infantPublishPrice": 0,
      "infantPublishTax": 0,
      "infantTax": 0,
      "infantTaxType": 0,
      "infantType": "",
      "itinerary": [
        {
          "destinationCity": "SEL",
          "duration": 29100,
          "originCity": "HKG",
          "segment": [
            {
              "accountCode": "",
              "aircraftCode": "321",
              "arrivalAirport": "PEK",
              "arrivalTerminal": "",
              "arrivalTime": "201909231620",
              "arrivalTimeWithOffset": "",
              "availabilitySource": "",
              "baggage": {
                "baggageCheck": false,
                "freeBaggagePiece": -1,
                "freeBaggageWeight": 20
              },
              "bookingClass": "S",
              "cabin": "E",
              "carrier": "CA",
              "childCabin": "",
              "childFareBasis": "",
              "codeShare": false,
              "connection": false,
              "departureAirport": "HKG",
              "departureTerminal": "",
              "departureTime": "201909231245",
              "departureTimeWithOffset": "",
              "duration": 215,
              "fareBasis": "WLORFHK6",
              "fareType": "PRIVATE",
              "flightNumber": "CA102",
              "flyTime": 0,
              "key": "",
              "mainSegment": true,
              "marriageGrp": "",
              "operatingCarrier": "CA",
              "operatingFlightNumber": "CA102",
              "seats": 1,
              "status": "",
              "stopCity": [],
              "stopInfo": 0
            },
            {
              "accountCode": "",
              "aircraftCode": "738",
              "arrivalAirport": "GMP",
              "arrivalTerminal": "",
              "arrivalTime": "201909232150",
              "arrivalTimeWithOffset": "",
              "availabilitySource": "",
              "baggage": {
                "baggageCheck": false,
                "freeBaggagePiece": -1,
                "freeBaggageWeight": 20
              },
              "bookingClass": "S",
              "cabin": "E",
              "carrier": "CA",
              "childCabin": "",
              "childFareBasis": "",
              "codeShare": false,
              "connection": false,
              "departureAirport": "PEK",
              "departureTerminal": "",
              "departureTime": "201909231845",
              "departureTimeWithOffset": "",
              "duration": 125,
              "fareBasis": "WLORFHK6",
              "fareType": "PRIVATE",
              "flightNumber": "CA137",
              "flyTime": 0,
              "key": "",
              "mainSegment": false,
              "marriageGrp": "",
              "operatingCarrier": "CA",
              "operatingFlightNumber": "CA137",
              "seats": 1,
              "status": "",
              "stopCity": [],
              "stopInfo": 0
            }
          ],
          "segmentSplicing": true
        }
      ],
      "itinerarySplicing": false,
      "masterCurrency": "CNY",
      "multiTicket": false,
      "nationalType": 0,
      "nationality": "",
      "onlineCheckIn": false,
      "oriAdultPrice": 244,
      "oriAdultTax": 0,
      "oriChildPrice": 244,
      "oriChildTax": 0,
      "oriInfantPrice": 0,
      "oriInfantTax": 0,
      "policyPriceChanges": [
        {
          "adultChange": {
            "absChange": {
              "amount": 4,
              "currency": "USD"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 0
            },
            "totalChange": {
              "amount": -56,
              "currency": "CNY"
            }
          },
          "childChange": {
            "absChange": {
              "amount": 4,
              "currency": "USD"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 0
            },
            "totalChange": {
              "amount": -56,
              "currency": "CNY"
            }
          },
          "displayNumber": "IC1908021687",
          "infantChange": null,
          "isFeeApplyToProvider": true,
          "otherAbsChangeDetails": [
            {
              "absTotal": {
                "amount": 10,
                "currency": "USD"
              },
              "desc": "INCENTIVE_RECEIVABLE",
              "totalChange": {
                "amount": 70,
                "currency": "CNY"
              }
            }
          ],
          "otherPercentageChangeDetails": [],
          "policyDesc": "IncentivePolicy:IC1908021687",
          "policyId": "5d4411fa73e1340001e3e890",
          "policyType": "INCENTIVE"
        },
        {
          "adultChange": {
            "absChange": {
              "amount": 5,
              "currency": "CNY"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 5.99
            },
            "totalChange": {
              "amount": 124.53019831932772,
              "currency": "CNY"
            }
          },
          "childChange": {
            "absChange": {
              "amount": 5,
              "currency": "CNY"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 5.99
            },
            "totalChange": {
              "amount": 124.53019831932772,
              "currency": "CNY"
            }
          },
          "displayNumber": "PF1907210860",
          "infantChange": {
            "absChange": {
              "amount": 5,
              "currency": "CNY"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 5.99
            },
            "totalChange": {
              "amount": 5.318583129454313,
              "currency": "CNY"
            }
          },
          "isFeeApplyToProvider": true,
          "otherAbsChangeDetails": [],
          "otherPercentageChangeDetails": [],
          "policyDesc": "PlatformPolicy:PF1907210860",
          "policyId": "5d342d9bf24d1c0001195a24",
          "policyType": "PLATFORM"
        }
      ],
      "posLocation": "CN",
      "priceType": 0,
      "providerCurrency": "EUR",
      "providerName": "skypk",
      "providerType": "PROVIDER_API",
      "routingId": "",
      "rule": {
        "changeBeforeDep": 0,
        "changeBeforeDepFee": 0,
        "changeDetail": null,
        "cnRemark": "",
        "currency": "CNY",
        "enRemark": "",
        "manualFareRule": null,
        "miniRule": -404,
        "noShowChange": 0,
        "noShowChangeAfter": 0,
        "noShowChangeAfterFee": 0,
        "noShowChangeFee": 0,
        "noShowRefund": 0,
        "noShowRefundAfter": 0,
        "noShowRefundAfterFee": 0,
        "noShowRefundFee": 0,
        "originRuleFee": {
          "changeAfterFee": -404,
          "changeAfterNoshowFee": -404,
          "changeBeforeFee": -404,
          "changeBeforeNoshowFee": -404,
          "currency": "",
          "refundAfterFee": -404,
          "refundAfterNoshowFee": -404,
          "refundBeforeFee": -404,
          "refundBeforeNoshowFee": -404
        },
        "partEndorse": 0,
        "partEndorsePrice": 0,
        "partRefund": 0,
        "partRefundFee": 0,
        "refundBeforeDep": 0,
        "refundBeforeDepFee": 0,
        "ruleFromOta": -404,
        "useOld": false
      },
      "saleBaggage": false,
      "seats": 1,
      "suitAge": "",
      "ticketInvoiceType": 0,
      "ticketPrice": 0,
      "ticketSource": 0,
      "ticketTimeLimitMinutes": 2880,
      "tof": "",
      "traceSpans": [
        {
          "application": "night-king",
          "createdAt": "2019-08-23T00:51:25.203359714Z",
          "desc": "move amount of 1.000000 from fare price to adult tax",
          "spanId": "468fb98f-7e1a-4089-bd56-0354c1ac74f2",
          "tags": {},
          "traceType": "None"
        },
        {
          "application": "night-king",
          "createdAt": "2019-08-23T00:51:25.203363015Z",
          "desc": "move amount of 1.000000 from child fare price to child tax",
          "spanId": "408d6375-f1e7-4491-b120-5dec18e9b585",
          "tags": {},
          "traceType": "None"
        }
      ],
      "validSegmentsCount": 2,
      "validatingCarrier": "CA",
      "viewPrice": 0
    },
    {
      "accountCode": "",
      "aduTag": "",
      "adultPrice": 2284.6983299648973,
      "adultPublishPrice": 2171.785,
      "adultPublishTax": 0,
      "adultTax": 1,
      "adultTaxType": 0,
      "adultType": "",
      "adultUoTax": 0,
      "adultYqTax": 0,
      "adultYrTax": 0,
      "applyType": 0,
      "arf": "",
      "bookingToken": "AcaMKuyCEo1jXVZho_xtPCmdjb2rlMZUp5zCUrScXvWpsQzU5dkxgfLqUPygGRDRDRX-8ikbWRHI_T_D8xjq34YwnH-KRiplEPumhbEN1WlL2hQl64dtt0WG7dHZ-4wuAvSdxzTB1gP11Mz6kfx0FWJespqg7__5V25fjtWuo5lP0_d_d_RCZe7FaebIhFKoZyHq2W9UHirplbqH--ICJ8mpRF9gUxR1D147NKgxnNGocfmtdkHFLS_KnQsEx7chMtKJT3aqo0WEviNZ7KajozJTtWMv-PtXzNPbAPf4sz179uQXLQd201UJlsC-Lm-xY2e_NXcLLTWOvVrsLf8gfqUZm5vtkgMLNbv44qwRNoCKAyC-o-ZxW4mAunGv7ZXN3lRCUQkDgh4RwMZ0SBbSvAaUemllL3uqLfJ5bCFirSXEF9RSHD3X1kigiFDYb9AmeQcD37tUfo-dbjWM6cXg5HQ==",
      "cabin": "E",
      "chiTag": "",
      "childFareBasis": "",
      "childPrice": 2284.6983299648973,
      "childPublishPrice": 2171.785,
      "childPublishTax": 0,
      "childTax": 1,
      "childTaxType": 0,
      "childTicketPrice": 0,
      "childType": "",
      "childUoTax": 0,
      "childYqTax": 0,
      "childYrTax": 0,
      "ctof": "",
      "currency": "CNY",
      "currencyConversions": [
        {
          "from": "EUR",
          "rate": 7.8974,
          "source": "BOC",
          "timestamp": "2019-08-23T00:37:25Z",
          "to": "CNY"
        },
        {
          "from": "USD",
          "rate": 7,
          "source": "MANUAL",
          "timestamp": "2019-08-14T07:46:00Z",
          "to": "CNY"
        }
      ],
      "data": "99b6660f-ac71-4a10-8745-dcc9b4cf1e76#9fcbc746-fd1d-4459-a622-b88d024a3c4d#OZ722_E",
      "eligibility": "",
      "evictionMarks": [
        {
          "evictionReason": "Platform[去哪人商旅] 航程内拼接",
          "traceSpans": [
            {
              "application": "night-king",
              "createdAt": null,
              "desc": "PlatformConfig filter",
              "spanId": "",
              "tags": {
                "DisplayNumber": "PFC1907306359",
                "Revision": "5"
              },
              "traceType": "None"
            }
          ]
        }
      ],
      "fareBasis": "",
      "fareCalcLine": "",
      "fareType": "PRIVATE",
      "flightCode": "",
      "infantPrice": 0,
      "infantPublishPrice": 0,
      "infantPublishTax": 0,
      "infantTax": 0,
      "infantTaxType": 0,
      "infantType": "",
      "itinerary": [
        {
          "destinationCity": "SEL",
          "duration": 12600,
          "originCity": "HKG",
          "segment": [
            {
              "accountCode": "",
              "aircraftCode": "333",
              "arrivalAirport": "ICN",
              "arrivalTerminal": "",
              "arrivalTime": "201909231740",
              "arrivalTimeWithOffset": "",
              "availabilitySource": "",
              "baggage": {
                "baggageCheck": false,
                "freeBaggagePiece": -1,
                "freeBaggageWeight": 23
              },
              "bookingClass": "L",
              "cabin": "E",
              "carrier": "OZ",
              "childCabin": "",
              "childFareBasis": "",
              "codeShare": false,
              "connection": false,
              "departureAirport": "HKG",
              "departureTerminal": "",
              "departureTime": "201909231310",
              "departureTimeWithOffset": "",
              "duration": 210,
              "fareBasis": "KLOSK",
              "fareType": "PRIVATE",
              "flightNumber": "OZ722",
              "flyTime": 0,
              "key": "",
              "mainSegment": true,
              "marriageGrp": "",
              "operatingCarrier": "OZ",
              "operatingFlightNumber": "OZ722",
              "seats": 1,
              "status": "",
              "stopCity": [],
              "stopInfo": 0
            }
          ],
          "segmentSplicing": true
        }
      ],
      "itinerarySplicing": false,
      "masterCurrency": "CNY",
      "multiTicket": false,
      "nationalType": 0,
      "nationality": "",
      "onlineCheckIn": true,
      "oriAdultPrice": 275,
      "oriAdultTax": 0,
      "oriChildPrice": 275,
      "oriChildTax": 0,
      "oriInfantPrice": 0,
      "oriInfantTax": 0,
      "policyPriceChanges": [
        {
          "adultChange": {
            "absChange": {
              "amount": 4,
              "currency": "USD"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 0
            },
            "totalChange": {
              "amount": -28,
              "currency": "CNY"
            }
          },
          "childChange": {
            "absChange": {
              "amount": 4,
              "currency": "USD"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 0
            },
            "totalChange": {
              "amount": -28,
              "currency": "CNY"
            }
          },
          "displayNumber": "IC1908021687",
          "infantChange": null,
          "isFeeApplyToProvider": true,
          "otherAbsChangeDetails": [
            {
              "absTotal": {
                "amount": 5,
                "currency": "USD"
              },
              "desc": "INCENTIVE_RECEIVABLE",
              "totalChange": {
                "amount": 35,
                "currency": "CNY"
              }
            }
          ],
          "otherPercentageChangeDetails": [],
          "policyDesc": "IncentivePolicy:IC1908021687",
          "policyId": "5d4411fa73e1340001e3e890",
          "policyType": "INCENTIVE"
        },
        {
          "adultChange": {
            "absChange": {
              "amount": 5,
              "currency": "CNY"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 5.99
            },
            "totalChange": {
              "amount": 141.91332996489734,
              "currency": "CNY"
            }
          },
          "childChange": {
            "absChange": {
              "amount": 5,
              "currency": "CNY"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 5.99
            },
            "totalChange": {
              "amount": 141.91332996489734,
              "currency": "CNY"
            }
          },
          "displayNumber": "PF1907210860",
          "infantChange": {
            "absChange": {
              "amount": 5,
              "currency": "CNY"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 5.99
            },
            "totalChange": {
              "amount": 5.318583129454313,
              "currency": "CNY"
            }
          },
          "isFeeApplyToProvider": true,
          "otherAbsChangeDetails": [],
          "otherPercentageChangeDetails": [],
          "policyDesc": "PlatformPolicy:PF1907210860",
          "policyId": "5d342d9bf24d1c0001195a24",
          "policyType": "PLATFORM"
        }
      ],
      "posLocation": "CN",
      "priceType": 0,
      "providerCurrency": "EUR",
      "providerName": "skypk",
      "providerType": "PROVIDER_API",
      "routingId": "",
      "rule": {
        "changeBeforeDep": 0,
        "changeBeforeDepFee": 0,
        "changeDetail": null,
        "cnRemark": "",
        "currency": "CNY",
        "enRemark": "",
        "manualFareRule": null,
        "miniRule": -404,
        "noShowChange": 0,
        "noShowChangeAfter": 0,
        "noShowChangeAfterFee": 0,
        "noShowChangeFee": 0,
        "noShowRefund": 0,
        "noShowRefundAfter": 0,
        "noShowRefundAfterFee": 0,
        "noShowRefundFee": 0,
        "originRuleFee": {
          "changeAfterFee": -404,
          "changeAfterNoshowFee": -404,
          "changeBeforeFee": -404,
          "changeBeforeNoshowFee": -404,
          "currency": "",
          "refundAfterFee": -404,
          "refundAfterNoshowFee": -404,
          "refundBeforeFee": -404,
          "refundBeforeNoshowFee": -404
        },
        "partEndorse": 0,
        "partEndorsePrice": 0,
        "partRefund": 0,
        "partRefundFee": 0,
        "refundBeforeDep": 0,
        "refundBeforeDepFee": 0,
        "ruleFromOta": -404,
        "useOld": false
      },
      "saleBaggage": false,
      "seats": 1,
      "suitAge": "",
      "ticketInvoiceType": 0,
      "ticketPrice": 0,
      "ticketSource": 0,
      "ticketTimeLimitMinutes": 2880,
      "tof": "",
      "traceSpans": [
        {
          "application": "night-king",
          "createdAt": "2019-08-23T00:51:25.203408229Z",
          "desc": "move amount of 1.000000 from fare price to adult tax",
          "spanId": "879adc0e-ed21-43ec-8e77-2882235ef96f",
          "tags": {},
          "traceType": "None"
        },
        {
          "application": "night-king",
          "createdAt": "2019-08-23T00:51:25.203411515Z",
          "desc": "move amount of 1.000000 from child fare price to child tax",
          "spanId": "ab6d3dd0-de87-474c-8813-08931fea17f1",
          "tags": {},
          "traceType": "None"
        }
      ],
      "validSegmentsCount": 1,
      "validatingCarrier": "OZ",
      "viewPrice": 0
    },
    {
      "accountCode": "",
      "aduTag": "",
      "adultPrice": 2284.6983299648973,
      "adultPublishPrice": 2171.785,
      "adultPublishTax": 0,
      "adultTax": 1,
      "adultTaxType": 0,
      "adultType": "",
      "adultUoTax": 0,
      "adultYqTax": 0,
      "adultYrTax": 0,
      "applyType": 0,
      "arf": "",
      "bookingToken": "A82BBM4jnNw3XxC7uP5UH1s6RCIVwljNxBU42CVwcIx05zt10JVmDCRaYO7r1aXQeW8bR1ZV3q9ghHvkox3SwdvnhmBqiuVuOV79M4QDbrNiH_WFvTdSqX1HVTmVfq0zljxlfyuPBQEoxkP8NQdovtkO0OtpQvQLedi92ZMA-7Hxi2quZs_0mjgr8PKIh75cP_h2e2JdNVjhxJkl-UxtofoR8FxdhtHL_virLgJrcBiuKPDmnqKmBn4rji7J2QVXG7URebbu_XVHP3b1t6BBqKchyDu79vRUOzagE7fvZ6G0i6OMAcgHLzmH7GWcGMWMhXOk7Ze9TYRntGxN7EerEqFQRG5lPFBza7rmjAF-KSlPbbTMPeFLvJeRyFJzJiZ80OQ_yf2widfnjSd-KkXls7j-tYGReQeYjoJkU4ksP7j9Y8M3P1R4xc1lo-JyEVONenwe79mVa5w_9NKllmBa3wA==",
      "cabin": "E",
      "chiTag": "",
      "childFareBasis": "",
      "childPrice": 2284.6983299648973,
      "childPublishPrice": 2171.785,
      "childPublishTax": 0,
      "childTax": 1,
      "childTaxType": 0,
      "childTicketPrice": 0,
      "childType": "",
      "childUoTax": 0,
      "childYqTax": 0,
      "childYrTax": 0,
      "ctof": "",
      "currency": "CNY",
      "currencyConversions": [
        {
          "from": "EUR",
          "rate": 7.8974,
          "source": "BOC",
          "timestamp": "2019-08-23T00:37:25Z",
          "to": "CNY"
        },
        {
          "from": "USD",
          "rate": 7,
          "source": "MANUAL",
          "timestamp": "2019-08-14T07:46:00Z",
          "to": "CNY"
        }
      ],
      "data": "99b6660f-ac71-4a10-8745-dcc9b4cf1e76#60be5bc2-c115-4da9-a6bc-23fab2cb5eb7#OZ746_E",
      "eligibility": "",
      "evictionMarks": [
        {
          "evictionReason": "Platform[去哪人商旅] 航程内拼接",
          "traceSpans": [
            {
              "application": "night-king",
              "createdAt": null,
              "desc": "PlatformConfig filter",
              "spanId": "",
              "tags": {
                "DisplayNumber": "PFC1907306359",
                "Revision": "5"
              },
              "traceType": "None"
            }
          ]
        }
      ],
      "fareBasis": "",
      "fareCalcLine": "",
      "fareType": "PRIVATE",
      "flightCode": "",
      "infantPrice": 0,
      "infantPublishPrice": 0,
      "infantPublishTax": 0,
      "infantTax": 0,
      "infantTaxType": 0,
      "infantType": "",
      "itinerary": [
        {
          "destinationCity": "SEL",
          "duration": 13200,
          "originCity": "HKG",
          "segment": [
            {
              "accountCode": "",
              "aircraftCode": "388",
              "arrivalAirport": "ICN",
              "arrivalTerminal": "",
              "arrivalTime": "201909230510",
              "arrivalTimeWithOffset": "",
              "availabilitySource": "",
              "baggage": {
                "baggageCheck": false,
                "freeBaggagePiece": -1,
                "freeBaggageWeight": 23
              },
              "bookingClass": "L",
              "cabin": "E",
              "carrier": "OZ",
              "childCabin": "",
              "childFareBasis": "",
              "codeShare": false,
              "connection": false,
              "departureAirport": "HKG",
              "departureTerminal": "",
              "departureTime": "201909230030",
              "departureTimeWithOffset": "",
              "duration": 220,
              "fareBasis": "KLOSK",
              "fareType": "PRIVATE",
              "flightNumber": "OZ746",
              "flyTime": 0,
              "key": "",
              "mainSegment": true,
              "marriageGrp": "",
              "operatingCarrier": "OZ",
              "operatingFlightNumber": "OZ746",
              "seats": 1,
              "status": "",
              "stopCity": [],
              "stopInfo": 0
            }
          ],
          "segmentSplicing": true
        }
      ],
      "itinerarySplicing": false,
      "masterCurrency": "CNY",
      "multiTicket": false,
      "nationalType": 0,
      "nationality": "",
      "onlineCheckIn": true,
      "oriAdultPrice": 275,
      "oriAdultTax": 0,
      "oriChildPrice": 275,
      "oriChildTax": 0,
      "oriInfantPrice": 0,
      "oriInfantTax": 0,
      "policyPriceChanges": [
        {
          "adultChange": {
            "absChange": {
              "amount": 4,
              "currency": "USD"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 0
            },
            "totalChange": {
              "amount": -28,
              "currency": "CNY"
            }
          },
          "childChange": {
            "absChange": {
              "amount": 4,
              "currency": "USD"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 0
            },
            "totalChange": {
              "amount": -28,
              "currency": "CNY"
            }
          },
          "displayNumber": "IC1908021687",
          "infantChange": null,
          "isFeeApplyToProvider": true,
          "otherAbsChangeDetails": [
            {
              "absTotal": {
                "amount": 5,
                "currency": "USD"
              },
              "desc": "INCENTIVE_RECEIVABLE",
              "totalChange": {
                "amount": 35,
                "currency": "CNY"
              }
            }
          ],
          "otherPercentageChangeDetails": [],
          "policyDesc": "IncentivePolicy:IC1908021687",
          "policyId": "5d4411fa73e1340001e3e890",
          "policyType": "INCENTIVE"
        },
        {
          "adultChange": {
            "absChange": {
              "amount": 5,
              "currency": "CNY"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 5.99
            },
            "totalChange": {
              "amount": 141.91332996489734,
              "currency": "CNY"
            }
          },
          "childChange": {
            "absChange": {
              "amount": 5,
              "currency": "CNY"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 5.99
            },
            "totalChange": {
              "amount": 141.91332996489734,
              "currency": "CNY"
            }
          },
          "displayNumber": "PF1907210860",
          "infantChange": {
            "absChange": {
              "amount": 5,
              "currency": "CNY"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 5.99
            },
            "totalChange": {
              "amount": 5.318583129454313,
              "currency": "CNY"
            }
          },
          "isFeeApplyToProvider": true,
          "otherAbsChangeDetails": [],
          "otherPercentageChangeDetails": [],
          "policyDesc": "PlatformPolicy:PF1907210860",
          "policyId": "5d342d9bf24d1c0001195a24",
          "policyType": "PLATFORM"
        }
      ],
      "posLocation": "CN",
      "priceType": 0,
      "providerCurrency": "EUR",
      "providerName": "skypk",
      "providerType": "PROVIDER_API",
      "routingId": "",
      "rule": {
        "changeBeforeDep": 0,
        "changeBeforeDepFee": 0,
        "changeDetail": null,
        "cnRemark": "",
        "currency": "CNY",
        "enRemark": "",
        "manualFareRule": null,
        "miniRule": -404,
        "noShowChange": 0,
        "noShowChangeAfter": 0,
        "noShowChangeAfterFee": 0,
        "noShowChangeFee": 0,
        "noShowRefund": 0,
        "noShowRefundAfter": 0,
        "noShowRefundAfterFee": 0,
        "noShowRefundFee": 0,
        "originRuleFee": {
          "changeAfterFee": -404,
          "changeAfterNoshowFee": -404,
          "changeBeforeFee": -404,
          "changeBeforeNoshowFee": -404,
          "currency": "",
          "refundAfterFee": -404,
          "refundAfterNoshowFee": -404,
          "refundBeforeFee": -404,
          "refundBeforeNoshowFee": -404
        },
        "partEndorse": 0,
        "partEndorsePrice": 0,
        "partRefund": 0,
        "partRefundFee": 0,
        "refundBeforeDep": 0,
        "refundBeforeDepFee": 0,
        "ruleFromOta": -404,
        "useOld": false
      },
      "saleBaggage": false,
      "seats": 1,
      "suitAge": "",
      "ticketInvoiceType": 0,
      "ticketPrice": 0,
      "ticketSource": 0,
      "ticketTimeLimitMinutes": 2880,
      "tof": "",
      "traceSpans": [
        {
          "application": "night-king",
          "createdAt": "2019-08-23T00:51:25.203455327Z",
          "desc": "move amount of 1.000000 from fare price to adult tax",
          "spanId": "1755023c-3792-44c7-bc19-8db940a968dc",
          "tags": {},
          "traceType": "None"
        },
        {
          "application": "night-king",
          "createdAt": "2019-08-23T00:51:25.203458606Z",
          "desc": "move amount of 1.000000 from child fare price to child tax",
          "spanId": "ff97ff03-793d-4b1d-9266-170de9c5f299",
          "tags": {},
          "traceType": "None"
        }
      ],
      "validSegmentsCount": 1,
      "validatingCarrier": "OZ",
      "viewPrice": 0
    },
    {
      "accountCode": "",
      "aduTag": "",
      "adultPrice": 2473.329752154026,
      "adultPublishPrice": 2377.1174,
      "adultPublishTax": 0,
      "adultTax": 1,
      "adultTaxType": 0,
      "adultType": "",
      "adultUoTax": 0,
      "adultYqTax": 0,
      "adultYrTax": 0,
      "applyType": 0,
      "arf": "",
      "bookingToken": "A5RGDEuXxFRHh9SW3V830SDXnYiEYakli4INFz0WIUagBrfgWm5eJBIvo60-bjpXVo8xG1S1uSzS7aTZTVj6c0mJSeOAm80vsC_RcYh-NzuuON54HIV7jD2pXyL13DJUrrcTa5fqmQ_P2fV-JX0GSnhai4gqmu5w7NYxzCnK3SOBEX7esvQrsPvdtp3S3sf5mjsVqn8s0qWqXngfT4NFpXkSmUjPwYZ-peG3raodXxrQYY52JAHMeAQCLIdsxah4Qi5SW3LLYf-DJLh6pCDbQUpzVDx3nJL_wIwDEwCIUNFg-E6c3YUdMMvQYf01ya4lBY3x2RFLbqRMYdSAxQ46nlRJ8j4qsm_SWAdlr4fuViaMwP58C3u4lIfS7R7am4_292mf55VgTCmLElLA3SOgwvFVIfUX5eN1Bl2QRE1B8ow5x2enptKTskOv9tDrnXHooLZuUQOE8oc3jofPWi9_o8lJPYllW5cK46I6UWyp7RgE=",
      "cabin": "E",
      "chiTag": "",
      "childFareBasis": "",
      "childPrice": 2473.329752154026,
      "childPublishPrice": 2377.1174,
      "childPublishTax": 0,
      "childTax": 1,
      "childTaxType": 0,
      "childTicketPrice": 0,
      "childType": "",
      "childUoTax": 0,
      "childYqTax": 0,
      "childYrTax": 0,
      "ctof": "",
      "currency": "CNY",
      "currencyConversions": [
        {
          "from": "EUR",
          "rate": 7.8974,
          "source": "BOC",
          "timestamp": "2019-08-23T00:37:25Z",
          "to": "CNY"
        },
        {
          "from": "USD",
          "rate": 7,
          "source": "MANUAL",
          "timestamp": "2019-08-14T07:46:00Z",
          "to": "CNY"
        }
      ],
      "data": "99b6660f-ac71-4a10-8745-dcc9b4cf1e76#7c1d4c64-1885-4ad8-ac94-dd5d8ce1fac1#BR828_E_7C2602_E",
      "eligibility": "",
      "evictionMarks": [
        {
          "evictionReason": "Platform[去哪人商旅] 航程内拼接",
          "traceSpans": [
            {
              "application": "night-king",
              "createdAt": null,
              "desc": "PlatformConfig filter",
              "spanId": "",
              "tags": {
                "DisplayNumber": "PFC1907306359",
                "Revision": "5"
              },
              "traceType": "None"
            }
          ]
        }
      ],
      "fareBasis": "",
      "fareCalcLine": "",
      "fareType": "PRIVATE",
      "flightCode": "",
      "infantPrice": 0,
      "infantPublishPrice": 0,
      "infantPublishTax": 0,
      "infantTax": 0,
      "infantTaxType": 0,
      "infantType": "",
      "itinerary": [
        {
          "destinationCity": "SEL",
          "duration": 24000,
          "originCity": "HKG",
          "segment": [
            {
              "accountCode": "",
              "aircraftCode": "321",
              "arrivalAirport": "TPE",
              "arrivalTerminal": "",
              "arrivalTime": "201909230910",
              "arrivalTimeWithOffset": "",
              "availabilitySource": "",
              "baggage": {
                "baggageCheck": false,
                "freeBaggagePiece": -1,
                "freeBaggageWeight": 0
              },
              "bookingClass": "S",
              "cabin": "E",
              "carrier": "BR",
              "childCabin": "",
              "childFareBasis": "",
              "codeShare": false,
              "connection": false,
              "departureAirport": "HKG",
              "departureTerminal": "",
              "departureTime": "201909230725",
              "departureTimeWithOffset": "",
              "duration": 105,
              "fareBasis": "",
              "fareType": "PRIVATE",
              "flightNumber": "BR828",
              "flyTime": 0,
              "key": "",
              "mainSegment": false,
              "marriageGrp": "",
              "operatingCarrier": "BR",
              "operatingFlightNumber": "BR828",
              "seats": 1,
              "status": "",
              "stopCity": [],
              "stopInfo": 0
            },
            {
              "accountCode": "",
              "aircraftCode": "",
              "arrivalAirport": "ICN",
              "arrivalTerminal": "",
              "arrivalTime": "201909231505",
              "arrivalTimeWithOffset": "",
              "availabilitySource": "",
              "baggage": {
                "baggageCheck": true,
                "freeBaggagePiece": -1,
                "freeBaggageWeight": 0
              },
              "bookingClass": "S",
              "cabin": "E",
              "carrier": "7C",
              "childCabin": "",
              "childFareBasis": "",
              "codeShare": false,
              "connection": false,
              "departureAirport": "TPE",
              "departureTerminal": "",
              "departureTime": "201909231135",
              "departureTimeWithOffset": "",
              "duration": 150,
              "fareBasis": "",
              "fareType": "PRIVATE",
              "flightNumber": "7C2602",
              "flyTime": 0,
              "key": "",
              "mainSegment": true,
              "marriageGrp": "",
              "operatingCarrier": "",
              "operatingFlightNumber": "",
              "seats": 1,
              "status": "",
              "stopCity": [],
              "stopInfo": 0
            }
          ],
          "segmentSplicing": true
        }
      ],
      "itinerarySplicing": false,
      "masterCurrency": "CNY",
      "multiTicket": false,
      "nationalType": 0,
      "nationality": "",
      "onlineCheckIn": false,
      "oriAdultPrice": 301,
      "oriAdultTax": 0,
      "oriChildPrice": 301,
      "oriChildTax": 0,
      "oriInfantPrice": 0,
      "oriInfantTax": 0,
      "policyPriceChanges": [
        {
          "adultChange": {
            "absChange": {
              "amount": 4,
              "currency": "USD"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 0
            },
            "totalChange": {
              "amount": -56,
              "currency": "CNY"
            }
          },
          "childChange": {
            "absChange": {
              "amount": 4,
              "currency": "USD"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 0
            },
            "totalChange": {
              "amount": -56,
              "currency": "CNY"
            }
          },
          "displayNumber": "IC1908021687",
          "infantChange": null,
          "isFeeApplyToProvider": true,
          "otherAbsChangeDetails": [
            {
              "absTotal": {
                "amount": 10,
                "currency": "USD"
              },
              "desc": "INCENTIVE_RECEIVABLE",
              "totalChange": {
                "amount": 70,
                "currency": "CNY"
              }
            }
          ],
          "otherPercentageChangeDetails": [],
          "policyDesc": "IncentivePolicy:IC1908021687",
          "policyId": "5d4411fa73e1340001e3e890",
          "policyType": "INCENTIVE"
        },
        {
          "adultChange": {
            "absChange": {
              "amount": 5,
              "currency": "CNY"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 5.99
            },
            "totalChange": {
              "amount": 153.21235215402618,
              "currency": "CNY"
            }
          },
          "childChange": {
            "absChange": {
              "amount": 5,
              "currency": "CNY"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 5.99
            },
            "totalChange": {
              "amount": 153.21235215402618,
              "currency": "CNY"
            }
          },
          "displayNumber": "PF1907210860",
          "infantChange": {
            "absChange": {
              "amount": 5,
              "currency": "CNY"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 5.99
            },
            "totalChange": {
              "amount": 5.318583129454313,
              "currency": "CNY"
            }
          },
          "isFeeApplyToProvider": true,
          "otherAbsChangeDetails": [],
          "otherPercentageChangeDetails": [],
          "policyDesc": "PlatformPolicy:PF1907210860",
          "policyId": "5d342d9bf24d1c0001195a24",
          "policyType": "PLATFORM"
        }
      ],
      "posLocation": "CN",
      "priceType": 0,
      "providerCurrency": "EUR",
      "providerName": "skypk",
      "providerType": "PROVIDER_API",
      "routingId": "",
      "rule": {
        "changeBeforeDep": 0,
        "changeBeforeDepFee": 0,
        "changeDetail": null,
        "cnRemark": "",
        "currency": "CNY",
        "enRemark": "",
        "manualFareRule": null,
        "miniRule": -404,
        "noShowChange": 0,
        "noShowChangeAfter": 0,
        "noShowChangeAfterFee": 0,
        "noShowChangeFee": 0,
        "noShowRefund": 0,
        "noShowRefundAfter": 0,
        "noShowRefundAfterFee": 0,
        "noShowRefundFee": 0,
        "originRuleFee": {
          "changeAfterFee": -404,
          "changeAfterNoshowFee": -404,
          "changeBeforeFee": -404,
          "changeBeforeNoshowFee": -404,
          "currency": "",
          "refundAfterFee": -404,
          "refundAfterNoshowFee": -404,
          "refundBeforeFee": -404,
          "refundBeforeNoshowFee": -404
        },
        "partEndorse": 0,
        "partEndorsePrice": 0,
        "partRefund": 0,
        "partRefundFee": 0,
        "refundBeforeDep": 0,
        "refundBeforeDepFee": 0,
        "ruleFromOta": -404,
        "useOld": false
      },
      "saleBaggage": false,
      "seats": 1,
      "suitAge": "",
      "ticketInvoiceType": 0,
      "ticketPrice": 0,
      "ticketSource": 0,
      "ticketTimeLimitMinutes": 2880,
      "tof": "",
      "traceSpans": [
        {
          "application": "night-king",
          "createdAt": "2019-08-23T00:51:25.203508864Z",
          "desc": "move amount of 1.000000 from fare price to adult tax",
          "spanId": "f620c9e0-a642-43c6-b651-c2d46e20f8c8",
          "tags": {},
          "traceType": "None"
        },
        {
          "application": "night-king",
          "createdAt": "2019-08-23T00:51:25.203512178Z",
          "desc": "move amount of 1.000000 from child fare price to child tax",
          "spanId": "968fb490-6145-4778-baca-31ac72433f62",
          "tags": {},
          "traceType": "None"
        }
      ],
      "validSegmentsCount": 2,
      "validatingCarrier": "BR",
      "viewPrice": 0
    },
    {
      "accountCode": "",
      "aduTag": "",
      "adultPrice": 2762.768322518881,
      "adultPublishPrice": 2677.2186,
      "adultPublishTax": 0,
      "adultTax": 1,
      "adultTaxType": 0,
      "adultType": "",
      "adultUoTax": 0,
      "adultYqTax": 0,
      "adultYrTax": 0,
      "applyType": 0,
      "arf": "",
      "bookingToken": "AIvMZRrDeVvSMuXmYPQe2O8Avd72WqyCX5OEGOkFtTaKvfJ4RMG2ZDyyNjg7kk_ikWiBLIiY5KpM0Bed3yi8R5LjcVt4qHdmj3O_9uGf38Letnju0Ov4nEDlD8hOn10YcjdokD4pKR1TuZqfrE92rj4pAg6Tz2yJwj366l2dlbJDRUNYIR7Bcce1BWOXdr1tmAgh1Yj8TZJWatWynOUGW3BAW-Jtq2EW_ZnGDjN5Al_x3aQKQ3cuB5lj5mK5XB_sTZVxREBnQkSMYgrf_tO436rEEtVhaWMSJU-mr_2pSricnXZmL-bw6M2YytTEg_9G0qAC_znrmmtqhgAzm9KWmebAQXZjaaVUbr74D82QESZ225E-OvCEpKPZPEQi14VdkuR16YbB066EQEDy46PbWETsKGnbbBNMnFNAHwzPH26_N--GoUpM4K58jxbf7j358ulRq5-p5_iLlgIZKi55In-YWzdS1sJYD5dFnOCg6nhng1yvBns4T5sthxhJPhVJob9RJZ6HxDXuddVSQWGi-iA==",
      "cabin": "E",
      "chiTag": "",
      "childFareBasis": "",
      "childPrice": 2762.768322518881,
      "childPublishPrice": 2677.2186,
      "childPublishTax": 0,
      "childTax": 1,
      "childTaxType": 0,
      "childTicketPrice": 0,
      "childType": "",
      "childUoTax": 0,
      "childYqTax": 0,
      "childYrTax": 0,
      "ctof": "",
      "currency": "CNY",
      "currencyConversions": [
        {
          "from": "EUR",
          "rate": 7.8974,
          "source": "BOC",
          "timestamp": "2019-08-23T00:37:25Z",
          "to": "CNY"
        },
        {
          "from": "USD",
          "rate": 7,
          "source": "MANUAL",
          "timestamp": "2019-08-14T07:46:00Z",
          "to": "CNY"
        }
      ],
      "data": "99b6660f-ac71-4a10-8745-dcc9b4cf1e76#c8412008-6a9b-493b-8129-f370f2bffcb1#CI934_E_TW674_E_KE1126_E",
      "eligibility": "",
      "evictionMarks": [
        {
          "evictionReason": "Platform[去哪人商旅] 航程内拼接",
          "traceSpans": [
            {
              "application": "night-king",
              "createdAt": null,
              "desc": "PlatformConfig filter",
              "spanId": "",
              "tags": {
                "DisplayNumber": "PFC1907306359",
                "Revision": "5"
              },
              "traceType": "None"
            }
          ]
        }
      ],
      "fareBasis": "",
      "fareCalcLine": "",
      "fareType": "PRIVATE",
      "flightCode": "",
      "infantPrice": 0,
      "infantPublishPrice": 0,
      "infantPublishTax": 0,
      "infantTax": 0,
      "infantTaxType": 0,
      "infantType": "",
      "itinerary": [
        {
          "destinationCity": "SEL",
          "duration": 37800,
          "originCity": "HKG",
          "segment": [
            {
              "accountCode": "",
              "aircraftCode": "333",
              "arrivalAirport": "KHH",
              "arrivalTerminal": "",
              "arrivalTime": "201909231145",
              "arrivalTimeWithOffset": "",
              "availabilitySource": "",
              "baggage": {
                "baggageCheck": false,
                "freeBaggagePiece": -1,
                "freeBaggageWeight": 0
              },
              "bookingClass": "S",
              "cabin": "E",
              "carrier": "CI",
              "childCabin": "",
              "childFareBasis": "",
              "codeShare": false,
              "connection": false,
              "departureAirport": "HKG",
              "departureTerminal": "",
              "departureTime": "201909231010",
              "departureTimeWithOffset": "",
              "duration": 95,
              "fareBasis": "",
              "fareType": "PRIVATE",
              "flightNumber": "CI934",
              "flyTime": 0,
              "key": "",
              "mainSegment": false,
              "marriageGrp": "",
              "operatingCarrier": "CI",
              "operatingFlightNumber": "CI934",
              "seats": 1,
              "status": "",
              "stopCity": [],
              "stopInfo": 0
            },
            {
              "accountCode": "",
              "aircraftCode": "737",
              "arrivalAirport": "PUS",
              "arrivalTerminal": "",
              "arrivalTime": "201909231830",
              "arrivalTimeWithOffset": "",
              "availabilitySource": "",
              "baggage": {
                "baggageCheck": true,
                "freeBaggagePiece": -1,
                "freeBaggageWeight": 0
              },
              "bookingClass": "S",
              "cabin": "E",
              "carrier": "TW",
              "childCabin": "",
              "childFareBasis": "",
              "codeShare": false,
              "connection": false,
              "departureAirport": "KHH",
              "departureTerminal": "",
              "departureTime": "201909231440",
              "departureTimeWithOffset": "",
              "duration": 170,
              "fareBasis": "ATG",
              "fareType": "PRIVATE",
              "flightNumber": "TW674",
              "flyTime": 0,
              "key": "",
              "mainSegment": true,
              "marriageGrp": "",
              "operatingCarrier": "TW",
              "operatingFlightNumber": "TW674",
              "seats": 1,
              "status": "",
              "stopCity": [],
              "stopInfo": 0
            },
            {
              "accountCode": "",
              "aircraftCode": "Non",
              "arrivalAirport": "GMP",
              "arrivalTerminal": "",
              "arrivalTime": "201909232140",
              "arrivalTimeWithOffset": "",
              "availabilitySource": "",
              "baggage": {
                "baggageCheck": true,
                "freeBaggagePiece": -1,
                "freeBaggageWeight": 0
              },
              "bookingClass": "N",
              "cabin": "E",
              "carrier": "KE",
              "childCabin": "",
              "childFareBasis": "",
              "codeShare": false,
              "connection": false,
              "departureAirport": "PUS",
              "departureTerminal": "",
              "departureTime": "201909232040",
              "departureTimeWithOffset": "",
              "duration": 60,
              "fareBasis": "Y",
              "fareType": "PRIVATE",
              "flightNumber": "KE1126",
              "flyTime": 0,
              "key": "",
              "mainSegment": false,
              "marriageGrp": "",
              "operatingCarrier": "KE",
              "operatingFlightNumber": "KE1126",
              "seats": 1,
              "status": "",
              "stopCity": [],
              "stopInfo": 0
            }
          ],
          "segmentSplicing": true
        }
      ],
      "itinerarySplicing": false,
      "masterCurrency": "CNY",
      "multiTicket": false,
      "nationalType": 0,
      "nationality": "",
      "onlineCheckIn": true,
      "oriAdultPrice": 339,
      "oriAdultTax": 0,
      "oriChildPrice": 339,
      "oriChildTax": 0,
      "oriInfantPrice": 0,
      "oriInfantTax": 0,
      "policyPriceChanges": [
        {
          "adultChange": {
            "absChange": {
              "amount": 4,
              "currency": "USD"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 0
            },
            "totalChange": {
              "amount": -84,
              "currency": "CNY"
            }
          },
          "childChange": {
            "absChange": {
              "amount": 4,
              "currency": "USD"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 0
            },
            "totalChange": {
              "amount": -84,
              "currency": "CNY"
            }
          },
          "displayNumber": "IC1908021687",
          "infantChange": null,
          "isFeeApplyToProvider": true,
          "otherAbsChangeDetails": [
            {
              "absTotal": {
                "amount": 15,
                "currency": "USD"
              },
              "desc": "INCENTIVE_RECEIVABLE",
              "totalChange": {
                "amount": 105,
                "currency": "CNY"
              }
            }
          ],
          "otherPercentageChangeDetails": [],
          "policyDesc": "IncentivePolicy:IC1908021687",
          "policyId": "5d4411fa73e1340001e3e890",
          "policyType": "INCENTIVE"
        },
        {
          "adultChange": {
            "absChange": {
              "amount": 5,
              "currency": "CNY"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 5.99
            },
            "totalChange": {
              "amount": 170.54972251888097,
              "currency": "CNY"
            }
          },
          "childChange": {
            "absChange": {
              "amount": 5,
              "currency": "CNY"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 5.99
            },
            "totalChange": {
              "amount": 170.54972251888097,
              "currency": "CNY"
            }
          },
          "displayNumber": "PF1907210860",
          "infantChange": {
            "absChange": {
              "amount": 5,
              "currency": "CNY"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 5.99
            },
            "totalChange": {
              "amount": 5.318583129454313,
              "currency": "CNY"
            }
          },
          "isFeeApplyToProvider": true,
          "otherAbsChangeDetails": [],
          "otherPercentageChangeDetails": [],
          "policyDesc": "PlatformPolicy:PF1907210860",
          "policyId": "5d342d9bf24d1c0001195a24",
          "policyType": "PLATFORM"
        }
      ],
      "posLocation": "CN",
      "priceType": 0,
      "providerCurrency": "EUR",
      "providerName": "skypk",
      "providerType": "PROVIDER_API",
      "routingId": "",
      "rule": {
        "changeBeforeDep": 0,
        "changeBeforeDepFee": 0,
        "changeDetail": null,
        "cnRemark": "",
        "currency": "CNY",
        "enRemark": "",
        "manualFareRule": null,
        "miniRule": -404,
        "noShowChange": 0,
        "noShowChangeAfter": 0,
        "noShowChangeAfterFee": 0,
        "noShowChangeFee": 0,
        "noShowRefund": 0,
        "noShowRefundAfter": 0,
        "noShowRefundAfterFee": 0,
        "noShowRefundFee": 0,
        "originRuleFee": {
          "changeAfterFee": -404,
          "changeAfterNoshowFee": -404,
          "changeBeforeFee": -404,
          "changeBeforeNoshowFee": -404,
          "currency": "",
          "refundAfterFee": -404,
          "refundAfterNoshowFee": -404,
          "refundBeforeFee": -404,
          "refundBeforeNoshowFee": -404
        },
        "partEndorse": 0,
        "partEndorsePrice": 0,
        "partRefund": 0,
        "partRefundFee": 0,
        "refundBeforeDep": 0,
        "refundBeforeDepFee": 0,
        "ruleFromOta": -404,
        "useOld": false
      },
      "saleBaggage": false,
      "seats": 1,
      "suitAge": "",
      "ticketInvoiceType": 0,
      "ticketPrice": 0,
      "ticketSource": 0,
      "ticketTimeLimitMinutes": 2880,
      "tof": "",
      "traceSpans": [
        {
          "application": "night-king",
          "createdAt": "2019-08-23T00:51:25.203558860Z",
          "desc": "move amount of 1.000000 from fare price to adult tax",
          "spanId": "40ce6f1f-4fb7-449f-88ae-7d3b38267227",
          "tags": {},
          "traceType": "None"
        },
        {
          "application": "night-king",
          "createdAt": "2019-08-23T00:51:25.203562105Z",
          "desc": "move amount of 1.000000 from child fare price to child tax",
          "spanId": "8ba2b963-312f-439e-ba29-f91423183033",
          "tags": {},
          "traceType": "None"
        }
      ],
      "validSegmentsCount": 3,
      "validatingCarrier": "CI",
      "viewPrice": 0
    },
    {
      "accountCode": "",
      "aduTag": "",
      "adultPrice": 2855.1748750132965,
      "adultPublishPrice": 2764.09,
      "adultPublishTax": 0,
      "adultTax": 1,
      "adultTaxType": 0,
      "adultType": "",
      "adultUoTax": 0,
      "adultYqTax": 0,
      "adultYrTax": 0,
      "applyType": 0,
      "arf": "",
      "bookingToken": "AnH4xPgMFbPOidZXSyzLCt6JLOxIV9i-8KXH2KfNUa1gwohfPLWRtSoX03RLoPQsZbUGq_hQIjp9gp3jmYtoCUBeO7QRomUaTg4nQcTouIByZd0Jn5gfxu8gvQAZavPf4TC-VZFTRF9EzRVWdlqTqDMBkHp6UVmByxbWd-0efTAlqznqaXJD-hGGH2vRhiZV2-xYGZopDVZ7Tx2KfbbHjqiWQ3IPeF3uPK53pZobUnU-zdyeicEs3yEj_S9S0db__gjNgFvaEiFzFydbX1fMwFT7oKXLFMeetLs5XJCsuLBXX_e1vlq3LvI0LrSeIOxnOoGZ5CG52KJWH5bOrit4eVulIys1yalOIbHv2I21HmDonE2FEZXy3ZDH8OdvRYfAOhyKQ0onK7MhIC4MdWkW4IJwr_1KR7BW28RWbvICqTxdilknFxFFXUoXGZasoZvkWmlfICo-UhVm4Vo4qPx1p9TrbKNcYS-o_xnoGMfJF-utemdrS_uweId_ZMvZ1rKJ1SaQLnCQiDabX__Brumux2w==",
      "cabin": "E",
      "chiTag": "",
      "childFareBasis": "",
      "childPrice": 2855.1748750132965,
      "childPublishPrice": 2764.09,
      "childPublishTax": 0,
      "childTax": 1,
      "childTaxType": 0,
      "childTicketPrice": 0,
      "childType": "",
      "childUoTax": 0,
      "childYqTax": 0,
      "childYrTax": 0,
      "ctof": "",
      "currency": "CNY",
      "currencyConversions": [
        {
          "from": "EUR",
          "rate": 7.8974,
          "source": "BOC",
          "timestamp": "2019-08-23T00:37:25Z",
          "to": "CNY"
        },
        {
          "from": "USD",
          "rate": 7,
          "source": "MANUAL",
          "timestamp": "2019-08-14T07:46:00Z",
          "to": "CNY"
        }
      ],
      "data": "99b6660f-ac71-4a10-8745-dcc9b4cf1e76#a7d4c4f9-358e-4427-8a33-daadad147f54#MU724_E_MU9829_E_BX8824_E",
      "eligibility": "",
      "evictionMarks": [
        {
          "evictionReason": "Platform[去哪人商旅] 航程内拼接",
          "traceSpans": [
            {
              "application": "night-king",
              "createdAt": null,
              "desc": "PlatformConfig filter",
              "spanId": "",
              "tags": {
                "DisplayNumber": "PFC1907306359",
                "Revision": "5"
              },
              "traceType": "None"
            }
          ]
        }
      ],
      "fareBasis": "",
      "fareCalcLine": "",
      "fareType": "PRIVATE",
      "flightCode": "",
      "infantPrice": 0,
      "infantPublishPrice": 0,
      "infantPublishTax": 0,
      "infantTax": 0,
      "infantTaxType": 0,
      "infantType": "",
      "itinerary": [
        {
          "destinationCity": "SEL",
          "duration": 33600,
          "originCity": "HKG",
          "segment": [
            {
              "accountCode": "",
              "aircraftCode": "321",
              "arrivalAirport": "PVG",
              "arrivalTerminal": "",
              "arrivalTime": "201909231150",
              "arrivalTimeWithOffset": "",
              "availabilitySource": "",
              "baggage": {
                "baggageCheck": false,
                "freeBaggagePiece": -1,
                "freeBaggageWeight": 15
              },
              "bookingClass": "Z",
              "cabin": "E",
              "carrier": "MU",
              "childCabin": "",
              "childFareBasis": "",
              "codeShare": false,
              "connection": false,
              "departureAirport": "HKG",
              "departureTerminal": "",
              "departureTime": "201909230935",
              "departureTimeWithOffset": "",
              "duration": 135,
              "fareBasis": "RSRWHKS",
              "fareType": "PRIVATE",
              "flightNumber": "MU724",
              "flyTime": 0,
              "key": "",
              "mainSegment": true,
              "marriageGrp": "",
              "operatingCarrier": "MU",
              "operatingFlightNumber": "MU724",
              "seats": 1,
              "status": "",
              "stopCity": [],
              "stopInfo": 0
            },
            {
              "accountCode": "",
              "aircraftCode": "738",
              "arrivalAirport": "PUS",
              "arrivalTerminal": "",
              "arrivalTime": "201909231650",
              "arrivalTimeWithOffset": "",
              "availabilitySource": "",
              "baggage": {
                "baggageCheck": false,
                "freeBaggagePiece": -1,
                "freeBaggageWeight": 15
              },
              "bookingClass": "Z",
              "cabin": "E",
              "carrier": "MU",
              "childCabin": "",
              "childFareBasis": "",
              "codeShare": true,
              "connection": false,
              "departureAirport": "PVG",
              "departureTerminal": "",
              "departureTime": "201909231350",
              "departureTimeWithOffset": "",
              "duration": 120,
              "fareBasis": "RSRWHKS",
              "fareType": "PRIVATE",
              "flightNumber": "MU9829",
              "flyTime": 0,
              "key": "",
              "mainSegment": false,
              "marriageGrp": "",
              "operatingCarrier": "FM",
              "operatingFlightNumber": "FM829",
              "seats": 1,
              "status": "",
              "stopCity": [],
              "stopInfo": 0
            },
            {
              "accountCode": "",
              "aircraftCode": "",
              "arrivalAirport": "GMP",
              "arrivalTerminal": "",
              "arrivalTime": "201909231955",
              "arrivalTimeWithOffset": "",
              "availabilitySource": "",
              "baggage": {
                "baggageCheck": true,
                "freeBaggagePiece": -1,
                "freeBaggageWeight": 15
              },
              "bookingClass": "G",
              "cabin": "E",
              "carrier": "BX",
              "childCabin": "",
              "childFareBasis": "",
              "codeShare": false,
              "connection": false,
              "departureAirport": "PUS",
              "departureTerminal": "",
              "departureTime": "201909231900",
              "departureTimeWithOffset": "",
              "duration": 55,
              "fareBasis": "",
              "fareType": "PRIVATE",
              "flightNumber": "BX8824",
              "flyTime": 0,
              "key": "",
              "mainSegment": false,
              "marriageGrp": "",
              "operatingCarrier": "",
              "operatingFlightNumber": "",
              "seats": 1,
              "status": "",
              "stopCity": [],
              "stopInfo": 0
            }
          ],
          "segmentSplicing": true
        }
      ],
      "itinerarySplicing": false,
      "masterCurrency": "CNY",
      "multiTicket": false,
      "nationalType": 0,
      "nationality": "",
      "onlineCheckIn": true,
      "oriAdultPrice": 350,
      "oriAdultTax": 0,
      "oriChildPrice": 350,
      "oriChildTax": 0,
      "oriInfantPrice": 0,
      "oriInfantTax": 0,
      "policyPriceChanges": [
        {
          "adultChange": {
            "absChange": {
              "amount": 4,
              "currency": "USD"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 0
            },
            "totalChange": {
              "amount": -84,
              "currency": "CNY"
            }
          },
          "childChange": {
            "absChange": {
              "amount": 4,
              "currency": "USD"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 0
            },
            "totalChange": {
              "amount": -84,
              "currency": "CNY"
            }
          },
          "displayNumber": "IC1908021687",
          "infantChange": null,
          "isFeeApplyToProvider": true,
          "otherAbsChangeDetails": [
            {
              "absTotal": {
                "amount": 15,
                "currency": "USD"
              },
              "desc": "INCENTIVE_RECEIVABLE",
              "totalChange": {
                "amount": 105,
                "currency": "CNY"
              }
            }
          ],
          "otherPercentageChangeDetails": [],
          "policyDesc": "IncentivePolicy:IC1908021687",
          "policyId": "5d4411fa73e1340001e3e890",
          "policyType": "INCENTIVE"
        },
        {
          "adultChange": {
            "absChange": {
              "amount": 5,
              "currency": "CNY"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 5.99
            },
            "totalChange": {
              "amount": 176.08487501329645,
              "currency": "CNY"
            }
          },
          "childChange": {
            "absChange": {
              "amount": 5,
              "currency": "CNY"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 5.99
            },
            "totalChange": {
              "amount": 176.08487501329645,
              "currency": "CNY"
            }
          },
          "displayNumber": "PF1907210860",
          "infantChange": {
            "absChange": {
              "amount": 5,
              "currency": "CNY"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 5.99
            },
            "totalChange": {
              "amount": 5.318583129454313,
              "currency": "CNY"
            }
          },
          "isFeeApplyToProvider": true,
          "otherAbsChangeDetails": [],
          "otherPercentageChangeDetails": [],
          "policyDesc": "PlatformPolicy:PF1907210860",
          "policyId": "5d342d9bf24d1c0001195a24",
          "policyType": "PLATFORM"
        }
      ],
      "posLocation": "CN",
      "priceType": 0,
      "providerCurrency": "EUR",
      "providerName": "skypk",
      "providerType": "PROVIDER_API",
      "routingId": "",
      "rule": {
        "changeBeforeDep": 0,
        "changeBeforeDepFee": 0,
        "changeDetail": null,
        "cnRemark": "",
        "currency": "CNY",
        "enRemark": "",
        "manualFareRule": null,
        "miniRule": -404,
        "noShowChange": 0,
        "noShowChangeAfter": 0,
        "noShowChangeAfterFee": 0,
        "noShowChangeFee": 0,
        "noShowRefund": 0,
        "noShowRefundAfter": 0,
        "noShowRefundAfterFee": 0,
        "noShowRefundFee": 0,
        "originRuleFee": {
          "changeAfterFee": -404,
          "changeAfterNoshowFee": -404,
          "changeBeforeFee": -404,
          "changeBeforeNoshowFee": -404,
          "currency": "",
          "refundAfterFee": -404,
          "refundAfterNoshowFee": -404,
          "refundBeforeFee": -404,
          "refundBeforeNoshowFee": -404
        },
        "partEndorse": 0,
        "partEndorsePrice": 0,
        "partRefund": 0,
        "partRefundFee": 0,
        "refundBeforeDep": 0,
        "refundBeforeDepFee": 0,
        "ruleFromOta": -404,
        "useOld": false
      },
      "saleBaggage": false,
      "seats": 1,
      "suitAge": "",
      "ticketInvoiceType": 0,
      "ticketPrice": 0,
      "ticketSource": 0,
      "ticketTimeLimitMinutes": 2880,
      "tof": "",
      "traceSpans": [
        {
          "application": "night-king",
          "createdAt": "2019-08-23T00:51:25.203605710Z",
          "desc": "move amount of 1.000000 from fare price to adult tax",
          "spanId": "d6165cb0-ebe1-4cee-a328-bce85df0b1f1",
          "tags": {},
          "traceType": "None"
        },
        {
          "application": "night-king",
          "createdAt": "2019-08-23T00:51:25.203609008Z",
          "desc": "move amount of 1.000000 from child fare price to child tax",
          "spanId": "ce003b64-7d1f-4c83-8c0e-4fd62f01cfcb",
          "tags": {},
          "traceType": "None"
        }
      ],
      "validSegmentsCount": 3,
      "validatingCarrier": "MU",
      "viewPrice": 0
    },
    {
      "accountCode": "",
      "aduTag": "",
      "adultPrice": 2922.3796404637806,
      "adultPublishPrice": 2827.2692,
      "adultPublishTax": 0,
      "adultTax": 1,
      "adultTaxType": 0,
      "adultType": "",
      "adultUoTax": 0,
      "adultYqTax": 0,
      "adultYrTax": 0,
      "applyType": 0,
      "arf": "",
      "bookingToken": "Ax15KYS3gWKVTzruXS8B45KR0o5jbymYifs7dM1p8TxC_nCuptOYgV10JdO_KbOZprEFRmLop8XdxTOMS1x1643zOnr_GQvGZW46hIdMvicO7AHOZ6yPMX4GGWCn_7J3sydOVkS6aK7qGKm16dkupfHqBv68LskKlOT69mFPVdVI-qIHVCJah3pNopNvC_GGmYF142jlk71q6EzOZg3SHe6YnhoYx0XXEwzNLOZkSlGyeK9axUd0R1C1aEA0e5DO83pG8BMwP8YTTXq3mnpzn6Cw75Q8qCN_gd_Yk9ZUa_K1HMeCeb_EeAdSQX9FcvhiuEYBqHeErYstx9WZhyhBZ7A6ZcZExRAgX6YQZDHCYmw2K22yrue9xMG6YIEN7-AGkbZmsJUfYKNyX2hZ_IleiRDeoliG6kDQfnKsTABc37WKXjM3JV7tC6Iu8navRM7pqGJvtTEeWGSvkCVwxG3h2K68B7hO2ReaetGJkktPGosmO3inxMrzoJOeuAUQZCaNfpDNNIClMizf1i2rzhu3QjFrslb4as12yDr8-81AndPE=",
      "cabin": "E",
      "chiTag": "",
      "childFareBasis": "",
      "childPrice": 2922.3796404637806,
      "childPublishPrice": 2827.2692,
      "childPublishTax": 0,
      "childTax": 1,
      "childTaxType": 0,
      "childTicketPrice": 0,
      "childType": "",
      "childUoTax": 0,
      "childYqTax": 0,
      "childYrTax": 0,
      "ctof": "",
      "currency": "CNY",
      "currencyConversions": [
        {
          "from": "EUR",
          "rate": 7.8974,
          "source": "BOC",
          "timestamp": "2019-08-23T00:37:25Z",
          "to": "CNY"
        },
        {
          "from": "USD",
          "rate": 7,
          "source": "MANUAL",
          "timestamp": "2019-08-14T07:46:00Z",
          "to": "CNY"
        }
      ],
      "data": "99b6660f-ac71-4a10-8745-dcc9b4cf1e76#670ab440-ad21-4db4-b5d2-519012f7b200#BR828_E_KE698_E_BX8820_E",
      "eligibility": "",
      "evictionMarks": [
        {
          "evictionReason": "Platform[去哪人商旅] 航程内拼接",
          "traceSpans": [
            {
              "application": "night-king",
              "createdAt": null,
              "desc": "PlatformConfig filter",
              "spanId": "",
              "tags": {
                "DisplayNumber": "PFC1907306359",
                "Revision": "5"
              },
              "traceType": "None"
            }
          ]
        }
      ],
      "fareBasis": "",
      "fareCalcLine": "",
      "fareType": "PRIVATE",
      "flightCode": "",
      "infantPrice": 0,
      "infantPublishPrice": 0,
      "infantPublishTax": 0,
      "infantTax": 0,
      "infantTaxType": 0,
      "infantType": "",
      "itinerary": [
        {
          "destinationCity": "SEL",
          "duration": 34200,
          "originCity": "HKG",
          "segment": [
            {
              "accountCode": "",
              "aircraftCode": "321",
              "arrivalAirport": "TPE",
              "arrivalTerminal": "",
              "arrivalTime": "201909230910",
              "arrivalTimeWithOffset": "",
              "availabilitySource": "",
              "baggage": {
                "baggageCheck": false,
                "freeBaggagePiece": -1,
                "freeBaggageWeight": 15
              },
              "bookingClass": "S",
              "cabin": "E",
              "carrier": "BR",
              "childCabin": "",
              "childFareBasis": "",
              "codeShare": false,
              "connection": false,
              "departureAirport": "HKG",
              "departureTerminal": "",
              "departureTime": "201909230725",
              "departureTimeWithOffset": "",
              "duration": 105,
              "fareBasis": "",
              "fareType": "PRIVATE",
              "flightNumber": "BR828",
              "flyTime": 0,
              "key": "",
              "mainSegment": false,
              "marriageGrp": "",
              "operatingCarrier": "BR",
              "operatingFlightNumber": "BR828",
              "seats": 1,
              "status": "",
              "stopCity": [],
              "stopInfo": 0
            },
            {
              "accountCode": "",
              "aircraftCode": "Non",
              "arrivalAirport": "PUS",
              "arrivalTerminal": "",
              "arrivalTime": "201909231500",
              "arrivalTimeWithOffset": "",
              "availabilitySource": "",
              "baggage": {
                "baggageCheck": true,
                "freeBaggagePiece": -1,
                "freeBaggageWeight": 15
              },
              "bookingClass": "N",
              "cabin": "E",
              "carrier": "KE",
              "childCabin": "",
              "childFareBasis": "",
              "codeShare": false,
              "connection": false,
              "departureAirport": "TPE",
              "departureTerminal": "",
              "departureTime": "201909231135",
              "departureTimeWithOffset": "",
              "duration": 145,
              "fareBasis": "ULE40RCK",
              "fareType": "PRIVATE",
              "flightNumber": "KE698",
              "flyTime": 0,
              "key": "",
              "mainSegment": true,
              "marriageGrp": "",
              "operatingCarrier": "KE",
              "operatingFlightNumber": "KE698",
              "seats": 1,
              "status": "",
              "stopCity": [],
              "stopInfo": 0
            },
            {
              "accountCode": "",
              "aircraftCode": "",
              "arrivalAirport": "GMP",
              "arrivalTerminal": "",
              "arrivalTime": "201909231755",
              "arrivalTimeWithOffset": "",
              "availabilitySource": "",
              "baggage": {
                "baggageCheck": true,
                "freeBaggagePiece": -1,
                "freeBaggageWeight": 15
              },
              "bookingClass": "G",
              "cabin": "E",
              "carrier": "BX",
              "childCabin": "",
              "childFareBasis": "",
              "codeShare": false,
              "connection": false,
              "departureAirport": "PUS",
              "departureTerminal": "",
              "departureTime": "201909231700",
              "departureTimeWithOffset": "",
              "duration": 55,
              "fareBasis": "",
              "fareType": "PRIVATE",
              "flightNumber": "BX8820",
              "flyTime": 0,
              "key": "",
              "mainSegment": false,
              "marriageGrp": "",
              "operatingCarrier": "",
              "operatingFlightNumber": "",
              "seats": 1,
              "status": "",
              "stopCity": [],
              "stopInfo": 0
            }
          ],
          "segmentSplicing": true
        }
      ],
      "itinerarySplicing": false,
      "masterCurrency": "CNY",
      "multiTicket": false,
      "nationalType": 0,
      "nationality": "",
      "onlineCheckIn": false,
      "oriAdultPrice": 358,
      "oriAdultTax": 0,
      "oriChildPrice": 358,
      "oriChildTax": 0,
      "oriInfantPrice": 0,
      "oriInfantTax": 0,
      "policyPriceChanges": [
        {
          "adultChange": {
            "absChange": {
              "amount": 4,
              "currency": "USD"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 0
            },
            "totalChange": {
              "amount": -84,
              "currency": "CNY"
            }
          },
          "childChange": {
            "absChange": {
              "amount": 4,
              "currency": "USD"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 0
            },
            "totalChange": {
              "amount": -84,
              "currency": "CNY"
            }
          },
          "displayNumber": "IC1908021687",
          "infantChange": null,
          "isFeeApplyToProvider": true,
          "otherAbsChangeDetails": [
            {
              "absTotal": {
                "amount": 15,
                "currency": "USD"
              },
              "desc": "INCENTIVE_RECEIVABLE",
              "totalChange": {
                "amount": 105,
                "currency": "CNY"
              }
            }
          ],
          "otherPercentageChangeDetails": [],
          "policyDesc": "IncentivePolicy:IC1908021687",
          "policyId": "5d4411fa73e1340001e3e890",
          "policyType": "INCENTIVE"
        },
        {
          "adultChange": {
            "absChange": {
              "amount": 5,
              "currency": "CNY"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 5.99
            },
            "totalChange": {
              "amount": 180.11044046378046,
              "currency": "CNY"
            }
          },
          "childChange": {
            "absChange": {
              "amount": 5,
              "currency": "CNY"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 5.99
            },
            "totalChange": {
              "amount": 180.11044046378046,
              "currency": "CNY"
            }
          },
          "displayNumber": "PF1907210860",
          "infantChange": {
            "absChange": {
              "amount": 5,
              "currency": "CNY"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 5.99
            },
            "totalChange": {
              "amount": 5.318583129454313,
              "currency": "CNY"
            }
          },
          "isFeeApplyToProvider": true,
          "otherAbsChangeDetails": [],
          "otherPercentageChangeDetails": [],
          "policyDesc": "PlatformPolicy:PF1907210860",
          "policyId": "5d342d9bf24d1c0001195a24",
          "policyType": "PLATFORM"
        }
      ],
      "posLocation": "CN",
      "priceType": 0,
      "providerCurrency": "EUR",
      "providerName": "skypk",
      "providerType": "PROVIDER_API",
      "routingId": "",
      "rule": {
        "changeBeforeDep": 0,
        "changeBeforeDepFee": 0,
        "changeDetail": null,
        "cnRemark": "",
        "currency": "CNY",
        "enRemark": "",
        "manualFareRule": null,
        "miniRule": -404,
        "noShowChange": 0,
        "noShowChangeAfter": 0,
        "noShowChangeAfterFee": 0,
        "noShowChangeFee": 0,
        "noShowRefund": 0,
        "noShowRefundAfter": 0,
        "noShowRefundAfterFee": 0,
        "noShowRefundFee": 0,
        "originRuleFee": {
          "changeAfterFee": -404,
          "changeAfterNoshowFee": -404,
          "changeBeforeFee": -404,
          "changeBeforeNoshowFee": -404,
          "currency": "",
          "refundAfterFee": -404,
          "refundAfterNoshowFee": -404,
          "refundBeforeFee": -404,
          "refundBeforeNoshowFee": -404
        },
        "partEndorse": 0,
        "partEndorsePrice": 0,
        "partRefund": 0,
        "partRefundFee": 0,
        "refundBeforeDep": 0,
        "refundBeforeDepFee": 0,
        "ruleFromOta": -404,
        "useOld": false
      },
      "saleBaggage": false,
      "seats": 1,
      "suitAge": "",
      "ticketInvoiceType": 0,
      "ticketPrice": 0,
      "ticketSource": 0,
      "ticketTimeLimitMinutes": 2880,
      "tof": "",
      "traceSpans": [
        {
          "application": "night-king",
          "createdAt": "2019-08-23T00:51:25.205167266Z",
          "desc": "move amount of 1.000000 from fare price to adult tax",
          "spanId": "3bee4d92-287f-4dbc-b0a5-1dfce6c37fa3",
          "tags": {},
          "traceType": "None"
        },
        {
          "application": "night-king",
          "createdAt": "2019-08-23T00:51:25.205170699Z",
          "desc": "move amount of 1.000000 from child fare price to child tax",
          "spanId": "58373892-4d3d-4757-90cf-5925a61ba458",
          "tags": {},
          "traceType": "None"
        }
      ],
      "validSegmentsCount": 3,
      "validatingCarrier": "BR",
      "viewPrice": 0
    },
    {
      "accountCode": "",
      "aduTag": "",
      "adultPrice": 2977.365493032656,
      "adultPublishPrice": 2850.9614,
      "adultPublishTax": 0,
      "adultTax": 1,
      "adultTaxType": 0,
      "adultType": "",
      "adultUoTax": 0,
      "adultYqTax": 0,
      "adultYrTax": 0,
      "applyType": 0,
      "arf": "",
      "bookingToken": "Ad-rtWow7T4xtyH5TMN2l0fwAPpiFt96HuOVWDX-WO0Hk1fhd_loOrPBSlClRxsU77k6y1De5-YouFOg_fhn57lHk9l8cmXSRok-1BOuB74mjSsvWSzpvFAaBHfEGhhxNd3npCU51BQS1uFFeaTgFHPcv9WzEfNMV7SLSLNU5x5052-1VyxJ_Zs6_FA02Fcb-HnLsRsLm2cos60PDhtMxg4THJ2Fprj_Ds6d2tpiSp7RjvrAFko_vTpisJ8wj8y1JL0gnFkRGY1FxyBLvqqLSzWpUOvpwhDMPtxvvugLc24rlUvy5hrBMim3r3xdMp1dpDj1NA518uYvVGJuStdly3C3AVA53DPIqIyg5tPYauQi4asKkWNZMK9hIec3c1chQBPe9MfBfcm3KdKdRo1XoVu2amXIloiW-Fd76jBGHmKRhyAYFxhRAGiRGNxUiEvZt-pSnkYm_fMlnHL2qsW43qybjeMCAHL1MVwYbZOoeR373gSxq5ckwnglS-RiijP4Zj7ZwPVIBjVntbMcs2bRWBw==",
      "cabin": "E",
      "chiTag": "",
      "childFareBasis": "",
      "childPrice": 2977.365493032656,
      "childPublishPrice": 2850.9614,
      "childPublishTax": 0,
      "childTax": 1,
      "childTaxType": 0,
      "childTicketPrice": 0,
      "childType": "",
      "childUoTax": 0,
      "childYqTax": 0,
      "childYrTax": 0,
      "ctof": "",
      "currency": "CNY",
      "currencyConversions": [
        {
          "from": "EUR",
          "rate": 7.8974,
          "source": "BOC",
          "timestamp": "2019-08-23T00:37:25Z",
          "to": "CNY"
        },
        {
          "from": "USD",
          "rate": 7,
          "source": "MANUAL",
          "timestamp": "2019-08-14T07:46:00Z",
          "to": "CNY"
        }
      ],
      "data": "99b6660f-ac71-4a10-8745-dcc9b4cf1e76#2e5fcae1-444f-4579-a1e2-04e91cb01f35#UO898_E_KE740_E",
      "eligibility": "",
      "evictionMarks": [
        {
          "evictionReason": "Platform[去哪人商旅] 航程内拼接",
          "traceSpans": [
            {
              "application": "night-king",
              "createdAt": null,
              "desc": "PlatformConfig filter",
              "spanId": "",
              "tags": {
                "DisplayNumber": "PFC1907306359",
                "Revision": "5"
              },
              "traceType": "None"
            }
          ]
        }
      ],
      "fareBasis": "",
      "fareCalcLine": "",
      "fareType": "PRIVATE",
      "flightCode": "",
      "infantPrice": 0,
      "infantPublishPrice": 0,
      "infantPublishTax": 0,
      "infantTax": 0,
      "infantTaxType": 0,
      "infantType": "",
      "itinerary": [
        {
          "destinationCity": "SEL",
          "duration": 32400,
          "originCity": "HKG",
          "segment": [
            {
              "accountCode": "",
              "aircraftCode": "",
              "arrivalAirport": "KIX",
              "arrivalTerminal": "",
              "arrivalTime": "201909231615",
              "arrivalTimeWithOffset": "",
              "availabilitySource": "",
              "baggage": {
                "baggageCheck": false,
                "freeBaggagePiece": -1,
                "freeBaggageWeight": 0
              },
              "bookingClass": "W",
              "cabin": "E",
              "carrier": "UO",
              "childCabin": "",
              "childFareBasis": "",
              "codeShare": false,
              "connection": false,
              "departureAirport": "HKG",
              "departureTerminal": "",
              "departureTime": "201909231120",
              "departureTimeWithOffset": "",
              "duration": 235,
              "fareBasis": "",
              "fareType": "PRIVATE",
              "flightNumber": "UO898",
              "flyTime": 0,
              "key": "",
              "mainSegment": true,
              "marriageGrp": "",
              "operatingCarrier": "",
              "operatingFlightNumber": "",
              "seats": 1,
              "status": "",
              "stopCity": [],
              "stopInfo": 0
            },
            {
              "accountCode": "",
              "aircraftCode": "772",
              "arrivalAirport": "GMP",
              "arrivalTerminal": "",
              "arrivalTime": "201909232120",
              "arrivalTimeWithOffset": "",
              "availabilitySource": "",
              "baggage": {
                "baggageCheck": true,
                "freeBaggagePiece": -1,
                "freeBaggageWeight": 0
              },
              "bookingClass": "N",
              "cabin": "E",
              "carrier": "KE",
              "childCabin": "",
              "childFareBasis": "",
              "codeShare": false,
              "connection": false,
              "departureAirport": "KIX",
              "departureTerminal": "",
              "departureTime": "201909231935",
              "departureTimeWithOffset": "",
              "duration": 105,
              "fareBasis": "NKX7ISJK",
              "fareType": "PRIVATE",
              "flightNumber": "KE740",
              "flyTime": 0,
              "key": "",
              "mainSegment": false,
              "marriageGrp": "",
              "operatingCarrier": "KE",
              "operatingFlightNumber": "KE740",
              "seats": 1,
              "status": "",
              "stopCity": [],
              "stopInfo": 0
            }
          ],
          "segmentSplicing": true
        }
      ],
      "itinerarySplicing": false,
      "masterCurrency": "CNY",
      "multiTicket": false,
      "nationalType": 0,
      "nationality": "",
      "onlineCheckIn": false,
      "oriAdultPrice": 361,
      "oriAdultTax": 0,
      "oriChildPrice": 361,
      "oriChildTax": 0,
      "oriInfantPrice": 0,
      "oriInfantTax": 0,
      "policyPriceChanges": [
        {
          "adultChange": {
            "absChange": {
              "amount": 4,
              "currency": "USD"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 0
            },
            "totalChange": {
              "amount": -56,
              "currency": "CNY"
            }
          },
          "childChange": {
            "absChange": {
              "amount": 4,
              "currency": "USD"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 0
            },
            "totalChange": {
              "amount": -56,
              "currency": "CNY"
            }
          },
          "displayNumber": "IC1908021687",
          "infantChange": null,
          "isFeeApplyToProvider": true,
          "otherAbsChangeDetails": [
            {
              "absTotal": {
                "amount": 10,
                "currency": "USD"
              },
              "desc": "INCENTIVE_RECEIVABLE",
              "totalChange": {
                "amount": 70,
                "currency": "CNY"
              }
            }
          ],
          "otherPercentageChangeDetails": [],
          "policyDesc": "IncentivePolicy:IC1908021687",
          "policyId": "5d4411fa73e1340001e3e890",
          "policyType": "INCENTIVE"
        },
        {
          "adultChange": {
            "absChange": {
              "amount": 5,
              "currency": "CNY"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 5.99
            },
            "totalChange": {
              "amount": 183.40409303265608,
              "currency": "CNY"
            }
          },
          "childChange": {
            "absChange": {
              "amount": 5,
              "currency": "CNY"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 5.99
            },
            "totalChange": {
              "amount": 183.40409303265608,
              "currency": "CNY"
            }
          },
          "displayNumber": "PF1907210860",
          "infantChange": {
            "absChange": {
              "amount": 5,
              "currency": "CNY"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 5.99
            },
            "totalChange": {
              "amount": 5.318583129454313,
              "currency": "CNY"
            }
          },
          "isFeeApplyToProvider": true,
          "otherAbsChangeDetails": [],
          "otherPercentageChangeDetails": [],
          "policyDesc": "PlatformPolicy:PF1907210860",
          "policyId": "5d342d9bf24d1c0001195a24",
          "policyType": "PLATFORM"
        }
      ],
      "posLocation": "CN",
      "priceType": 0,
      "providerCurrency": "EUR",
      "providerName": "skypk",
      "providerType": "PROVIDER_API",
      "routingId": "",
      "rule": {
        "changeBeforeDep": 0,
        "changeBeforeDepFee": 0,
        "changeDetail": null,
        "cnRemark": "",
        "currency": "CNY",
        "enRemark": "",
        "manualFareRule": null,
        "miniRule": -404,
        "noShowChange": 0,
        "noShowChangeAfter": 0,
        "noShowChangeAfterFee": 0,
        "noShowChangeFee": 0,
        "noShowRefund": 0,
        "noShowRefundAfter": 0,
        "noShowRefundAfterFee": 0,
        "noShowRefundFee": 0,
        "originRuleFee": {
          "changeAfterFee": -404,
          "changeAfterNoshowFee": -404,
          "changeBeforeFee": -404,
          "changeBeforeNoshowFee": -404,
          "currency": "",
          "refundAfterFee": -404,
          "refundAfterNoshowFee": -404,
          "refundBeforeFee": -404,
          "refundBeforeNoshowFee": -404
        },
        "partEndorse": 0,
        "partEndorsePrice": 0,
        "partRefund": 0,
        "partRefundFee": 0,
        "refundBeforeDep": 0,
        "refundBeforeDepFee": 0,
        "ruleFromOta": -404,
        "useOld": false
      },
      "saleBaggage": false,
      "seats": 1,
      "suitAge": "",
      "ticketInvoiceType": 0,
      "ticketPrice": 0,
      "ticketSource": 0,
      "ticketTimeLimitMinutes": 2880,
      "tof": "",
      "traceSpans": [
        {
          "application": "night-king",
          "createdAt": "2019-08-23T00:51:25.203710451Z",
          "desc": "move amount of 1.000000 from fare price to adult tax",
          "spanId": "73fbbd7a-1691-4f75-b655-ea0388a628be",
          "tags": {},
          "traceType": "None"
        },
        {
          "application": "night-king",
          "createdAt": "2019-08-23T00:51:25.203713662Z",
          "desc": "move amount of 1.000000 from child fare price to child tax",
          "spanId": "e6f1c80e-a1f2-4a5d-89f0-3b883802d1f8",
          "tags": {},
          "traceType": "None"
        }
      ],
      "validSegmentsCount": 2,
      "validatingCarrier": "UO",
      "viewPrice": 0
    },
    {
      "accountCode": "",
      "aduTag": "",
      "adultPrice": 3220.9827677906605,
      "adultPublishPrice": 3079.986,
      "adultPublishTax": 0,
      "adultTax": 1,
      "adultTaxType": 0,
      "adultType": "",
      "adultUoTax": 0,
      "adultYqTax": 0,
      "adultYrTax": 0,
      "applyType": 0,
      "arf": "",
      "bookingToken": "AcOWblsztJYMu6z7DXE0t5h79esNXWUBaLlqYMxbs3PwFcajabt1rbFlyPZkNaEuVLycrGNpWQriQSgXWrpPhPeQdDlreVQZSzFOwoJf9vADegX2IkqbiSRnXesu8eWfKe8h2NOcVppZsJ6E9QhZK4HzlweByfVDKwyYROuZbpK8tzuE_WZxAlz8fYxVZOiMo5XGBFTqAyBttWp3SdR9SOg8aa2DWmJ9AAmZZDIAElv6Y4i_DtkFZKuAGEA1JQaJaZsdO48KbcKzYeV8zf7XUYokUGXP8V110M6M-Ny1pfTivEMg8lpEyz3Wph-uq2WT6JGfBsjFzWWdxAb1RgRrtxauY4VtcSJ7P8OWzWowaHghTqOShk-ouBL_OLDOV_PcjdTkEYYF_SeXMb0v_UUp-JsHMwabp6fiaXiZwHUPjHHP6lJxNtH5EaXAXVDcVdh94VAlvoneJzBFgoiFglqumA1ODKVtHyMfj9ZRuD1_J6gFXY3QemV2bC6FFrSzEAOCH8mT1pxBASBDaWTBDltXctg==",
      "cabin": "E",
      "chiTag": "",
      "childFareBasis": "",
      "childPrice": 3220.9827677906605,
      "childPublishPrice": 3079.986,
      "childPublishTax": 0,
      "childTax": 1,
      "childTaxType": 0,
      "childTicketPrice": 0,
      "childType": "",
      "childUoTax": 0,
      "childYqTax": 0,
      "childYrTax": 0,
      "ctof": "",
      "currency": "CNY",
      "currencyConversions": [
        {
          "from": "EUR",
          "rate": 7.8974,
          "source": "BOC",
          "timestamp": "2019-08-23T00:37:25Z",
          "to": "CNY"
        },
        {
          "from": "USD",
          "rate": 7,
          "source": "MANUAL",
          "timestamp": "2019-08-14T07:46:00Z",
          "to": "CNY"
        }
      ],
      "data": "99b6660f-ac71-4a10-8745-dcc9b4cf1e76#92e95ea2-ee40-4a3c-b9f3-e7f4e031b092#FM722_E_OZ3625_E",
      "eligibility": "",
      "evictionMarks": [
        {
          "evictionReason": "Platform[去哪人商旅] 航程内拼接",
          "traceSpans": [
            {
              "application": "night-king",
              "createdAt": null,
              "desc": "PlatformConfig filter",
              "spanId": "",
              "tags": {
                "DisplayNumber": "PFC1907306359",
                "Revision": "5"
              },
              "traceType": "None"
            }
          ]
        }
      ],
      "fareBasis": "",
      "fareCalcLine": "",
      "fareType": "PRIVATE",
      "flightCode": "",
      "infantPrice": 0,
      "infantPublishPrice": 0,
      "infantPublishTax": 0,
      "infantTax": 0,
      "infantTaxType": 0,
      "infantType": "",
      "itinerary": [
        {
          "destinationCity": "SEL",
          "duration": 28500,
          "originCity": "HKG",
          "segment": [
            {
              "accountCode": "",
              "aircraftCode": "321",
              "arrivalAirport": "SHA",
              "arrivalTerminal": "",
              "arrivalTime": "201909231440",
              "arrivalTimeWithOffset": "",
              "availabilitySource": "",
              "baggage": {
                "baggageCheck": false,
                "freeBaggagePiece": -1,
                "freeBaggageWeight": 20
              },
              "bookingClass": "S",
              "cabin": "E",
              "carrier": "FM",
              "childCabin": "",
              "childFareBasis": "",
              "codeShare": true,
              "connection": false,
              "departureAirport": "HKG",
              "departureTerminal": "",
              "departureTime": "201909231205",
              "departureTimeWithOffset": "",
              "duration": 155,
              "fareBasis": "VSB02MS2",
              "fareType": "PRIVATE",
              "flightNumber": "FM722",
              "flyTime": 0,
              "key": "",
              "mainSegment": true,
              "marriageGrp": "",
              "operatingCarrier": "MU",
              "operatingFlightNumber": "MU722",
              "seats": 1,
              "status": "",
              "stopCity": [],
              "stopInfo": 0
            },
            {
              "accountCode": "",
              "aircraftCode": "333",
              "arrivalAirport": "GMP",
              "arrivalTerminal": "",
              "arrivalTime": "201909232100",
              "arrivalTimeWithOffset": "",
              "availabilitySource": "",
              "baggage": {
                "baggageCheck": true,
                "freeBaggagePiece": -1,
                "freeBaggageWeight": 20
              },
              "bookingClass": "L",
              "cabin": "E",
              "carrier": "OZ",
              "childCabin": "",
              "childFareBasis": "",
              "codeShare": false,
              "connection": false,
              "departureAirport": "SHA",
              "departureTerminal": "",
              "departureTime": "201909231800",
              "departureTimeWithOffset": "",
              "duration": 120,
              "fareBasis": "",
              "fareType": "PRIVATE",
              "flightNumber": "OZ3625",
              "flyTime": 0,
              "key": "",
              "mainSegment": false,
              "marriageGrp": "",
              "operatingCarrier": "OZ",
              "operatingFlightNumber": "OZ3625",
              "seats": 1,
              "status": "",
              "stopCity": [],
              "stopInfo": 0
            }
          ],
          "segmentSplicing": true
        }
      ],
      "itinerarySplicing": false,
      "masterCurrency": "CNY",
      "multiTicket": false,
      "nationalType": 0,
      "nationality": "",
      "onlineCheckIn": false,
      "oriAdultPrice": 390,
      "oriAdultTax": 0,
      "oriChildPrice": 390,
      "oriChildTax": 0,
      "oriInfantPrice": 0,
      "oriInfantTax": 0,
      "policyPriceChanges": [
        {
          "adultChange": {
            "absChange": {
              "amount": 4,
              "currency": "USD"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 0
            },
            "totalChange": {
              "amount": -56,
              "currency": "CNY"
            }
          },
          "childChange": {
            "absChange": {
              "amount": 4,
              "currency": "USD"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 0
            },
            "totalChange": {
              "amount": -56,
              "currency": "CNY"
            }
          },
          "displayNumber": "IC1908021687",
          "infantChange": null,
          "isFeeApplyToProvider": true,
          "otherAbsChangeDetails": [
            {
              "absTotal": {
                "amount": 10,
                "currency": "USD"
              },
              "desc": "INCENTIVE_RECEIVABLE",
              "totalChange": {
                "amount": 70,
                "currency": "CNY"
              }
            }
          ],
          "otherPercentageChangeDetails": [],
          "policyDesc": "IncentivePolicy:IC1908021687",
          "policyId": "5d4411fa73e1340001e3e890",
          "policyType": "INCENTIVE"
        },
        {
          "adultChange": {
            "absChange": {
              "amount": 5,
              "currency": "CNY"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 5.99
            },
            "totalChange": {
              "amount": 197.99676779066058,
              "currency": "CNY"
            }
          },
          "childChange": {
            "absChange": {
              "amount": 5,
              "currency": "CNY"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 5.99
            },
            "totalChange": {
              "amount": 197.99676779066058,
              "currency": "CNY"
            }
          },
          "displayNumber": "PF1907210860",
          "infantChange": {
            "absChange": {
              "amount": 5,
              "currency": "CNY"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 5.99
            },
            "totalChange": {
              "amount": 5.318583129454313,
              "currency": "CNY"
            }
          },
          "isFeeApplyToProvider": true,
          "otherAbsChangeDetails": [],
          "otherPercentageChangeDetails": [],
          "policyDesc": "PlatformPolicy:PF1907210860",
          "policyId": "5d342d9bf24d1c0001195a24",
          "policyType": "PLATFORM"
        }
      ],
      "posLocation": "CN",
      "priceType": 0,
      "providerCurrency": "EUR",
      "providerName": "skypk",
      "providerType": "PROVIDER_API",
      "routingId": "",
      "rule": {
        "changeBeforeDep": 0,
        "changeBeforeDepFee": 0,
        "changeDetail": null,
        "cnRemark": "",
        "currency": "CNY",
        "enRemark": "",
        "manualFareRule": null,
        "miniRule": -404,
        "noShowChange": 0,
        "noShowChangeAfter": 0,
        "noShowChangeAfterFee": 0,
        "noShowChangeFee": 0,
        "noShowRefund": 0,
        "noShowRefundAfter": 0,
        "noShowRefundAfterFee": 0,
        "noShowRefundFee": 0,
        "originRuleFee": {
          "changeAfterFee": -404,
          "changeAfterNoshowFee": -404,
          "changeBeforeFee": -404,
          "changeBeforeNoshowFee": -404,
          "currency": "",
          "refundAfterFee": -404,
          "refundAfterNoshowFee": -404,
          "refundBeforeFee": -404,
          "refundBeforeNoshowFee": -404
        },
        "partEndorse": 0,
        "partEndorsePrice": 0,
        "partRefund": 0,
        "partRefundFee": 0,
        "refundBeforeDep": 0,
        "refundBeforeDepFee": 0,
        "ruleFromOta": -404,
        "useOld": false
      },
      "saleBaggage": false,
      "seats": 1,
      "suitAge": "",
      "ticketInvoiceType": 0,
      "ticketPrice": 0,
      "ticketSource": 0,
      "ticketTimeLimitMinutes": 2880,
      "tof": "",
      "traceSpans": [
        {
          "application": "night-king",
          "createdAt": "2019-08-23T00:51:25.203795365Z",
          "desc": "move amount of 1.000000 from fare price to adult tax",
          "spanId": "cf91a818-87ed-4140-87f6-bed5e93dafb1",
          "tags": {},
          "traceType": "None"
        },
        {
          "application": "night-king",
          "createdAt": "2019-08-23T00:51:25.203798629Z",
          "desc": "move amount of 1.000000 from child fare price to child tax",
          "spanId": "8d23a483-ec8e-41e3-bbdf-88cdb04bba24",
          "tags": {},
          "traceType": "None"
        }
      ],
      "validSegmentsCount": 2,
      "validatingCarrier": "FM",
      "viewPrice": 0
    },
    {
      "accountCode": "",
      "aduTag": "",
      "adultPrice": 3233.201680672269,
      "adultPublishPrice": 3119.473,
      "adultPublishTax": 0,
      "adultTax": 1,
      "adultTaxType": 0,
      "adultType": "",
      "adultUoTax": 0,
      "adultYqTax": 0,
      "adultYrTax": 0,
      "applyType": 0,
      "arf": "",
      "bookingToken": "A0ifxxXSDH81FuCMU_zQT_lRtXMtZwGmfDoHVvF_hlO1YoFtHpsJrsreA-AEgPlsSYMjo-0ADeeMyxKxZWrZgCpfIZh1JIZnavdPXkARnjWIqNNX7uCsnRrtbDDHNsZbhUyhTNOBe-J2nfc6xjwlrzOgHxt03sHrlYD0rGuFSnU_vX3B4xpBgiPnMcUiqPn7MuxidO6I0PKpLblv3QsxD6OLQN9tdbpIe3448_mTzRa4cdrUPYvzNbs7LgTJ5Yr3kO2Y4URD4s8y79ZOgtmcD0FI-QO7sjaXhp9aEPcF5pCAtBYKqVGN1hijIcpaG6eTVSkyQItE6GGde99_x6hAjovrz2Pb_htClaofGBxJ79neFaw6i-97NQbgM-v-K_WtAsPy1LFxlFp4VVVLyYNlSRFSVcS3issAni2i5roPxL2EC5S2dDVIIjFM8IEPvZHLkcR52RFolghDWgYzZYX3vCUGYWyOEwoUK0Mw7bfklVayMTJuIE1Rt0STLTV3oQizKPeX52SjUM0Qiv5B1ohkQQQ==",
      "cabin": "E",
      "chiTag": "",
      "childFareBasis": "",
      "childPrice": 3233.201680672269,
      "childPublishPrice": 3119.473,
      "childPublishTax": 0,
      "childTax": 1,
      "childTaxType": 0,
      "childTicketPrice": 0,
      "childType": "",
      "childUoTax": 0,
      "childYqTax": 0,
      "childYrTax": 0,
      "ctof": "",
      "currency": "CNY",
      "currencyConversions": [
        {
          "from": "EUR",
          "rate": 7.8974,
          "source": "BOC",
          "timestamp": "2019-08-23T00:37:25Z",
          "to": "CNY"
        },
        {
          "from": "USD",
          "rate": 7,
          "source": "MANUAL",
          "timestamp": "2019-08-14T07:46:00Z",
          "to": "CNY"
        }
      ],
      "data": "99b6660f-ac71-4a10-8745-dcc9b4cf1e76#3b3a4f2f-b209-420e-8efd-486e09277fef#BR828_E_KE698_E_KE1118_E",
      "eligibility": "",
      "evictionMarks": [
        {
          "evictionReason": "Platform[去哪人商旅] 航程内拼接",
          "traceSpans": [
            {
              "application": "night-king",
              "createdAt": null,
              "desc": "PlatformConfig filter",
              "spanId": "",
              "tags": {
                "DisplayNumber": "PFC1907306359",
                "Revision": "5"
              },
              "traceType": "None"
            }
          ]
        }
      ],
      "fareBasis": "",
      "fareCalcLine": "",
      "fareType": "PRIVATE",
      "flightCode": "",
      "infantPrice": 0,
      "infantPublishPrice": 0,
      "infantPublishTax": 0,
      "infantTax": 0,
      "infantTaxType": 0,
      "infantType": "",
      "itinerary": [
        {
          "destinationCity": "SEL",
          "duration": 33300,
          "originCity": "HKG",
          "segment": [
            {
              "accountCode": "",
              "aircraftCode": "321",
              "arrivalAirport": "TPE",
              "arrivalTerminal": "",
              "arrivalTime": "201909230910",
              "arrivalTimeWithOffset": "",
              "availabilitySource": "",
              "baggage": {
                "baggageCheck": false,
                "freeBaggagePiece": -1,
                "freeBaggageWeight": 20
              },
              "bookingClass": "S",
              "cabin": "E",
              "carrier": "BR",
              "childCabin": "",
              "childFareBasis": "",
              "codeShare": false,
              "connection": false,
              "departureAirport": "HKG",
              "departureTerminal": "",
              "departureTime": "201909230725",
              "departureTimeWithOffset": "",
              "duration": 105,
              "fareBasis": "",
              "fareType": "PRIVATE",
              "flightNumber": "BR828",
              "flyTime": 0,
              "key": "",
              "mainSegment": false,
              "marriageGrp": "",
              "operatingCarrier": "BR",
              "operatingFlightNumber": "BR828",
              "seats": 1,
              "status": "",
              "stopCity": [],
              "stopInfo": 0
            },
            {
              "accountCode": "",
              "aircraftCode": "Non",
              "arrivalAirport": "PUS",
              "arrivalTerminal": "",
              "arrivalTime": "201909231500",
              "arrivalTimeWithOffset": "",
              "availabilitySource": "",
              "baggage": {
                "baggageCheck": true,
                "freeBaggagePiece": -1,
                "freeBaggageWeight": 20
              },
              "bookingClass": "N",
              "cabin": "E",
              "carrier": "KE",
              "childCabin": "",
              "childFareBasis": "",
              "codeShare": false,
              "connection": false,
              "departureAirport": "TPE",
              "departureTerminal": "",
              "departureTime": "201909231135",
              "departureTimeWithOffset": "",
              "duration": 145,
              "fareBasis": "ULE40RCK",
              "fareType": "PRIVATE",
              "flightNumber": "KE698",
              "flyTime": 0,
              "key": "",
              "mainSegment": true,
              "marriageGrp": "",
              "operatingCarrier": "KE",
              "operatingFlightNumber": "KE698",
              "seats": 1,
              "status": "",
              "stopCity": [],
              "stopInfo": 0
            },
            {
              "accountCode": "",
              "aircraftCode": "739",
              "arrivalAirport": "GMP",
              "arrivalTerminal": "",
              "arrivalTime": "201909231740",
              "arrivalTimeWithOffset": "",
              "availabilitySource": "",
              "baggage": {
                "baggageCheck": false,
                "freeBaggagePiece": -1,
                "freeBaggageWeight": 20
              },
              "bookingClass": "N",
              "cabin": "E",
              "carrier": "KE",
              "childCabin": "",
              "childFareBasis": "",
              "codeShare": false,
              "connection": false,
              "departureAirport": "PUS",
              "departureTerminal": "",
              "departureTime": "201909231640",
              "departureTimeWithOffset": "",
              "duration": 60,
              "fareBasis": "YKE",
              "fareType": "PRIVATE",
              "flightNumber": "KE1118",
              "flyTime": 0,
              "key": "",
              "mainSegment": false,
              "marriageGrp": "",
              "operatingCarrier": "KE",
              "operatingFlightNumber": "KE1118",
              "seats": 1,
              "status": "",
              "stopCity": [],
              "stopInfo": 0
            }
          ],
          "segmentSplicing": true
        }
      ],
      "itinerarySplicing": false,
      "masterCurrency": "CNY",
      "multiTicket": false,
      "nationalType": 0,
      "nationality": "",
      "onlineCheckIn": false,
      "oriAdultPrice": 395,
      "oriAdultTax": 0,
      "oriChildPrice": 395,
      "oriChildTax": 0,
      "oriInfantPrice": 0,
      "oriInfantTax": 0,
      "policyPriceChanges": [
        {
          "adultChange": {
            "absChange": {
              "amount": 4,
              "currency": "USD"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 0
            },
            "totalChange": {
              "amount": -84,
              "currency": "CNY"
            }
          },
          "childChange": {
            "absChange": {
              "amount": 4,
              "currency": "USD"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 0
            },
            "totalChange": {
              "amount": -84,
              "currency": "CNY"
            }
          },
          "displayNumber": "IC1908021687",
          "infantChange": null,
          "isFeeApplyToProvider": true,
          "otherAbsChangeDetails": [
            {
              "absTotal": {
                "amount": 15,
                "currency": "USD"
              },
              "desc": "INCENTIVE_RECEIVABLE",
              "totalChange": {
                "amount": 105,
                "currency": "CNY"
              }
            }
          ],
          "otherPercentageChangeDetails": [],
          "policyDesc": "IncentivePolicy:IC1908021687",
          "policyId": "5d4411fa73e1340001e3e890",
          "policyType": "INCENTIVE"
        },
        {
          "adultChange": {
            "absChange": {
              "amount": 5,
              "currency": "CNY"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 5.99
            },
            "totalChange": {
              "amount": 198.7286806722689,
              "currency": "CNY"
            }
          },
          "childChange": {
            "absChange": {
              "amount": 5,
              "currency": "CNY"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 5.99
            },
            "totalChange": {
              "amount": 198.7286806722689,
              "currency": "CNY"
            }
          },
          "displayNumber": "PF1907210860",
          "infantChange": {
            "absChange": {
              "amount": 5,
              "currency": "CNY"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 5.99
            },
            "totalChange": {
              "amount": 5.318583129454313,
              "currency": "CNY"
            }
          },
          "isFeeApplyToProvider": true,
          "otherAbsChangeDetails": [],
          "otherPercentageChangeDetails": [],
          "policyDesc": "PlatformPolicy:PF1907210860",
          "policyId": "5d342d9bf24d1c0001195a24",
          "policyType": "PLATFORM"
        }
      ],
      "posLocation": "CN",
      "priceType": 0,
      "providerCurrency": "EUR",
      "providerName": "skypk",
      "providerType": "PROVIDER_API",
      "routingId": "",
      "rule": {
        "changeBeforeDep": 0,
        "changeBeforeDepFee": 0,
        "changeDetail": null,
        "cnRemark": "",
        "currency": "CNY",
        "enRemark": "",
        "manualFareRule": null,
        "miniRule": -404,
        "noShowChange": 0,
        "noShowChangeAfter": 0,
        "noShowChangeAfterFee": 0,
        "noShowChangeFee": 0,
        "noShowRefund": 0,
        "noShowRefundAfter": 0,
        "noShowRefundAfterFee": 0,
        "noShowRefundFee": 0,
        "originRuleFee": {
          "changeAfterFee": -404,
          "changeAfterNoshowFee": -404,
          "changeBeforeFee": -404,
          "changeBeforeNoshowFee": -404,
          "currency": "",
          "refundAfterFee": -404,
          "refundAfterNoshowFee": -404,
          "refundBeforeFee": -404,
          "refundBeforeNoshowFee": -404
        },
        "partEndorse": 0,
        "partEndorsePrice": 0,
        "partRefund": 0,
        "partRefundFee": 0,
        "refundBeforeDep": 0,
        "refundBeforeDepFee": 0,
        "ruleFromOta": -404,
        "useOld": false
      },
      "saleBaggage": false,
      "seats": 1,
      "suitAge": "",
      "ticketInvoiceType": 0,
      "ticketPrice": 0,
      "ticketSource": 0,
      "ticketTimeLimitMinutes": 2880,
      "tof": "",
      "traceSpans": [
        {
          "application": "night-king",
          "createdAt": "2019-08-23T00:51:25.204078649Z",
          "desc": "move amount of 1.000000 from fare price to adult tax",
          "spanId": "56eb293f-3eb7-4579-9ec6-2ffcf16f0159",
          "tags": {},
          "traceType": "None"
        },
        {
          "application": "night-king",
          "createdAt": "2019-08-23T00:51:25.204081968Z",
          "desc": "move amount of 1.000000 from child fare price to child tax",
          "spanId": "a6aeef7f-5f50-47ce-b480-d7c4200b48ae",
          "tags": {},
          "traceType": "None"
        }
      ],
      "validSegmentsCount": 3,
      "validatingCarrier": "BR",
      "viewPrice": 0
    },
    {
      "accountCode": "",
      "aduTag": "",
      "adultPrice": 3237.7839591532816,
      "adultPublishPrice": 3095.7808,
      "adultPublishTax": 0,
      "adultTax": 1,
      "adultTaxType": 0,
      "adultType": "",
      "adultUoTax": 0,
      "adultYqTax": 0,
      "adultYrTax": 0,
      "applyType": 0,
      "arf": "",
      "bookingToken": "Amv-BWVnd_ckfcGl8w0FbBPIC1m8UOwx0BAXcvRCEqfN260ZCgF11MLj0sgxDSIiCYdGtjGY1Af-93A1r2F7Cqg378iBCqTe5r96mgElPmqiPO3waGgDj89VuPH0QGzTcRrA2AdtNnmpZNYg6KPS4S-5XdKkJuJ8DFkcksM_i-uR3vFFmSR0iAkuVjvyvJ8-5TyTUwy99if-dx4m3g_-v2BRDryDvaDKzfBhWa-jOoFj3s5dXiBDpc7zExANK3IBNzethIpLc9Po8lSBFdsk3d0t0BV_ANjwBWUH5rfzG3z5hYl33SKIz9wvfAf1-skQo3fZgXq6o-PRoGjG9f1ZpUdxeDNdSwg7jw-HoERkEljdbgiQ8jdw1NLyYbGTct5MQCklQ-ukD7a1zuWbfvXJ_PWnAZCWnsDVArphhXN2QYRhG-G5CR8wMbjE7sxPfduzSSZYUqftSWJ2l1dr6jRPCDQVBerSQjs3Mb0RXLaqtPkWkkB3sKZmDDdQTUSK_oQ-fiLxCN4JhdgUDLXyxfEdVbQ==",
      "cabin": "E",
      "chiTag": "",
      "childFareBasis": "",
      "childPrice": 3237.7839591532816,
      "childPublishPrice": 3095.7808,
      "childPublishTax": 0,
      "childTax": 1,
      "childTaxType": 0,
      "childTicketPrice": 0,
      "childType": "",
      "childUoTax": 0,
      "childYqTax": 0,
      "childYrTax": 0,
      "ctof": "",
      "currency": "CNY",
      "currencyConversions": [
        {
          "from": "EUR",
          "rate": 7.8974,
          "source": "BOC",
          "timestamp": "2019-08-23T00:37:25Z",
          "to": "CNY"
        },
        {
          "from": "USD",
          "rate": 7,
          "source": "MANUAL",
          "timestamp": "2019-08-14T07:46:00Z",
          "to": "CNY"
        }
      ],
      "data": "99b6660f-ac71-4a10-8745-dcc9b4cf1e76#b53c0122-1c7d-4253-b098-d3872fac8997#MU5018_E_KE816_E",
      "eligibility": "",
      "evictionMarks": [
        {
          "evictionReason": "Platform[去哪人商旅] 航程内拼接",
          "traceSpans": [
            {
              "application": "night-king",
              "createdAt": null,
              "desc": "PlatformConfig filter",
              "spanId": "",
              "tags": {
                "DisplayNumber": "PFC1907306359",
                "Revision": "5"
              },
              "traceType": "None"
            }
          ]
        }
      ],
      "fareBasis": "",
      "fareCalcLine": "",
      "fareType": "PRIVATE",
      "flightCode": "",
      "infantPrice": 0,
      "infantPublishPrice": 0,
      "infantPublishTax": 0,
      "infantTax": 0,
      "infantTaxType": 0,
      "infantType": "",
      "itinerary": [
        {
          "destinationCity": "SEL",
          "duration": 24600,
          "originCity": "HKG",
          "segment": [
            {
              "accountCode": "",
              "aircraftCode": "333",
              "arrivalAirport": "SHA",
              "arrivalTerminal": "",
              "arrivalTime": "201909231605",
              "arrivalTimeWithOffset": "",
              "availabilitySource": "",
              "baggage": {
                "baggageCheck": false,
                "freeBaggagePiece": -1,
                "freeBaggageWeight": 20
              },
              "bookingClass": "Z",
              "cabin": "E",
              "carrier": "MU",
              "childCabin": "",
              "childFareBasis": "",
              "codeShare": false,
              "connection": false,
              "departureAirport": "HKG",
              "departureTerminal": "",
              "departureTime": "201909231340",
              "departureTimeWithOffset": "",
              "duration": 145,
              "fareBasis": "TLE72BS2",
              "fareType": "PRIVATE",
              "flightNumber": "MU5018",
              "flyTime": 0,
              "key": "",
              "mainSegment": true,
              "marriageGrp": "",
              "operatingCarrier": "MU",
              "operatingFlightNumber": "MU5018",
              "seats": 1,
              "status": "",
              "stopCity": [],
              "stopInfo": 0
            },
            {
              "accountCode": "",
              "aircraftCode": "77W",
              "arrivalAirport": "GMP",
              "arrivalTerminal": "",
              "arrivalTime": "201909232130",
              "arrivalTimeWithOffset": "",
              "availabilitySource": "",
              "baggage": {
                "baggageCheck": true,
                "freeBaggagePiece": -1,
                "freeBaggageWeight": 20
              },
              "bookingClass": "N",
              "cabin": "E",
              "carrier": "KE",
              "childCabin": "",
              "childFareBasis": "",
              "codeShare": false,
              "connection": false,
              "departureAirport": "SHA",
              "departureTerminal": "",
              "departureTime": "201909231825",
              "departureTimeWithOffset": "",
              "duration": 125,
              "fareBasis": "KLE00RCK",
              "fareType": "PRIVATE",
              "flightNumber": "KE816",
              "flyTime": 0,
              "key": "",
              "mainSegment": false,
              "marriageGrp": "",
              "operatingCarrier": "KE",
              "operatingFlightNumber": "KE816",
              "seats": 1,
              "status": "",
              "stopCity": [],
              "stopInfo": 0
            }
          ],
          "segmentSplicing": true
        }
      ],
      "itinerarySplicing": false,
      "masterCurrency": "CNY",
      "multiTicket": false,
      "nationalType": 0,
      "nationality": "",
      "onlineCheckIn": true,
      "oriAdultPrice": 392,
      "oriAdultTax": 0,
      "oriChildPrice": 392,
      "oriChildTax": 0,
      "oriInfantPrice": 0,
      "oriInfantTax": 0,
      "policyPriceChanges": [
        {
          "adultChange": {
            "absChange": {
              "amount": 4,
              "currency": "USD"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 0
            },
            "totalChange": {
              "amount": -56,
              "currency": "CNY"
            }
          },
          "childChange": {
            "absChange": {
              "amount": 4,
              "currency": "USD"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 0
            },
            "totalChange": {
              "amount": -56,
              "currency": "CNY"
            }
          },
          "displayNumber": "IC1908021687",
          "infantChange": null,
          "isFeeApplyToProvider": true,
          "otherAbsChangeDetails": [
            {
              "absTotal": {
                "amount": 10,
                "currency": "USD"
              },
              "desc": "INCENTIVE_RECEIVABLE",
              "totalChange": {
                "amount": 70,
                "currency": "CNY"
              }
            }
          ],
          "otherPercentageChangeDetails": [],
          "policyDesc": "IncentivePolicy:IC1908021687",
          "policyId": "5d4411fa73e1340001e3e890",
          "policyType": "INCENTIVE"
        },
        {
          "adultChange": {
            "absChange": {
              "amount": 5,
              "currency": "CNY"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 5.99
            },
            "totalChange": {
              "amount": 199.00315915328156,
              "currency": "CNY"
            }
          },
          "childChange": {
            "absChange": {
              "amount": 5,
              "currency": "CNY"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 5.99
            },
            "totalChange": {
              "amount": 199.00315915328156,
              "currency": "CNY"
            }
          },
          "displayNumber": "PF1907210860",
          "infantChange": {
            "absChange": {
              "amount": 5,
              "currency": "CNY"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 5.99
            },
            "totalChange": {
              "amount": 5.318583129454313,
              "currency": "CNY"
            }
          },
          "isFeeApplyToProvider": true,
          "otherAbsChangeDetails": [],
          "otherPercentageChangeDetails": [],
          "policyDesc": "PlatformPolicy:PF1907210860",
          "policyId": "5d342d9bf24d1c0001195a24",
          "policyType": "PLATFORM"
        }
      ],
      "posLocation": "CN",
      "priceType": 0,
      "providerCurrency": "EUR",
      "providerName": "skypk",
      "providerType": "PROVIDER_API",
      "routingId": "",
      "rule": {
        "changeBeforeDep": 0,
        "changeBeforeDepFee": 0,
        "changeDetail": null,
        "cnRemark": "",
        "currency": "CNY",
        "enRemark": "",
        "manualFareRule": null,
        "miniRule": -404,
        "noShowChange": 0,
        "noShowChangeAfter": 0,
        "noShowChangeAfterFee": 0,
        "noShowChangeFee": 0,
        "noShowRefund": 0,
        "noShowRefundAfter": 0,
        "noShowRefundAfterFee": 0,
        "noShowRefundFee": 0,
        "originRuleFee": {
          "changeAfterFee": -404,
          "changeAfterNoshowFee": -404,
          "changeBeforeFee": -404,
          "changeBeforeNoshowFee": -404,
          "currency": "",
          "refundAfterFee": -404,
          "refundAfterNoshowFee": -404,
          "refundBeforeFee": -404,
          "refundBeforeNoshowFee": -404
        },
        "partEndorse": 0,
        "partEndorsePrice": 0,
        "partRefund": 0,
        "partRefundFee": 0,
        "refundBeforeDep": 0,
        "refundBeforeDepFee": 0,
        "ruleFromOta": -404,
        "useOld": false
      },
      "saleBaggage": false,
      "seats": 1,
      "suitAge": "",
      "ticketInvoiceType": 0,
      "ticketPrice": 0,
      "ticketSource": 0,
      "ticketTimeLimitMinutes": 2880,
      "tof": "",
      "traceSpans": [
        {
          "application": "night-king",
          "createdAt": "2019-08-23T00:51:25.203858374Z",
          "desc": "move amount of 1.000000 from fare price to adult tax",
          "spanId": "38d47d28-3159-4414-be99-a6a4615968ee",
          "tags": {},
          "traceType": "None"
        },
        {
          "application": "night-king",
          "createdAt": "2019-08-23T00:51:25.203861735Z",
          "desc": "move amount of 1.000000 from child fare price to child tax",
          "spanId": "8f5f9223-a2f8-4757-863b-6b3c0dd55fbf",
          "tags": {},
          "traceType": "None"
        }
      ],
      "validSegmentsCount": 2,
      "validatingCarrier": "MU",
      "viewPrice": 0
    },
    {
      "accountCode": "",
      "aduTag": "",
      "adultPrice": 3304.9887246037656,
      "adultPublishPrice": 3158.96,
      "adultPublishTax": 0,
      "adultTax": 1,
      "adultTaxType": 0,
      "adultType": "",
      "adultUoTax": 0,
      "adultYqTax": 0,
      "adultYrTax": 0,
      "applyType": 0,
      "arf": "",
      "bookingToken": "AmRoGm1J0UNwoAb-qczw33a02ZNYSXVDsKv_UrOv0y9-3AYIxmuYdlxGojV80l3h6CkRKnTimE99UX4bguDh-wrdpD7ef1G-l643JurMLruy1pYKYfIpsuSPKcpvx4HMCF9WSbNHI1XaCkqFmB_WG4DSMCYc3aYszjrDYjO24xs9OmOzOPWITD8hpiWd66OrKeNhzXVXLsZcQuZvIApEN5rrrfWjmzHKMoJWFMRKynqVn_-GNZOzlXkZBrUt7_bSjNUi84CsgUR1bwWfeqfo-8jjdMxOJ4d0mAUpeVFyF36TDgOd_wf5ZcGb5OWwFApWX2iGD3P1pA3zaE2d0ICwQ2nXf5psaeGN9QeRMrGXQOTeYjpQtnYwCcNsED0OPWTYYgHnnoYEsoZ0R2MWcolPqyh8i_XwYArcaX0oFAtVgIye3hi5FJp_rkk0RybBoGfXYkHuVx_uAt4GlGHKuzVAj__fXWOW6fQo4bSQvThz_xqU26TaMWmkIp4PvndVrqI-5",
      "cabin": "E",
      "chiTag": "",
      "childFareBasis": "",
      "childPrice": 3304.9887246037656,
      "childPublishPrice": 3158.96,
      "childPublishTax": 0,
      "childTax": 1,
      "childTaxType": 0,
      "childTicketPrice": 0,
      "childType": "",
      "childUoTax": 0,
      "childYqTax": 0,
      "childYrTax": 0,
      "ctof": "",
      "currency": "CNY",
      "currencyConversions": [
        {
          "from": "EUR",
          "rate": 7.8974,
          "source": "BOC",
          "timestamp": "2019-08-23T00:37:25Z",
          "to": "CNY"
        },
        {
          "from": "USD",
          "rate": 7,
          "source": "MANUAL",
          "timestamp": "2019-08-14T07:46:00Z",
          "to": "CNY"
        }
      ],
      "data": "99b6660f-ac71-4a10-8745-dcc9b4cf1e76#7a44af5c-e328-4fc2-8c1b-9cc87d2e9140#MM64_E_KE740_E",
      "eligibility": "",
      "evictionMarks": [
        {
          "evictionReason": "Platform[去哪人商旅] 航程内拼接",
          "traceSpans": [
            {
              "application": "night-king",
              "createdAt": null,
              "desc": "PlatformConfig filter",
              "spanId": "",
              "tags": {
                "DisplayNumber": "PFC1907306359",
                "Revision": "5"
              },
              "traceType": "None"
            }
          ]
        }
      ],
      "fareBasis": "",
      "fareCalcLine": "",
      "fareType": "PRIVATE",
      "flightCode": "",
      "infantPrice": 0,
      "infantPublishPrice": 0,
      "infantPublishTax": 0,
      "infantTax": 0,
      "infantTaxType": 0,
      "infantType": "",
      "itinerary": [
        {
          "destinationCity": "SEL",
          "duration": 27600,
          "originCity": "HKG",
          "segment": [
            {
              "accountCode": "",
              "aircraftCode": "",
              "arrivalAirport": "KIX",
              "arrivalTerminal": "",
              "arrivalTime": "201909231730",
              "arrivalTimeWithOffset": "",
              "availabilitySource": "",
              "baggage": {
                "baggageCheck": false,
                "freeBaggagePiece": -1,
                "freeBaggageWeight": 0
              },
              "bookingClass": "V",
              "cabin": "E",
              "carrier": "MM",
              "childCabin": "",
              "childFareBasis": "",
              "codeShare": false,
              "connection": false,
              "departureAirport": "HKG",
              "departureTerminal": "",
              "departureTime": "201909231240",
              "departureTimeWithOffset": "",
              "duration": 230,
              "fareBasis": "",
              "fareType": "PRIVATE",
              "flightNumber": "MM64",
              "flyTime": 0,
              "key": "",
              "mainSegment": true,
              "marriageGrp": "",
              "operatingCarrier": "",
              "operatingFlightNumber": "",
              "seats": 1,
              "status": "",
              "stopCity": [],
              "stopInfo": 0
            },
            {
              "accountCode": "",
              "aircraftCode": "772",
              "arrivalAirport": "GMP",
              "arrivalTerminal": "",
              "arrivalTime": "201909232120",
              "arrivalTimeWithOffset": "",
              "availabilitySource": "",
              "baggage": {
                "baggageCheck": true,
                "freeBaggagePiece": -1,
                "freeBaggageWeight": 0
              },
              "bookingClass": "N",
              "cabin": "E",
              "carrier": "KE",
              "childCabin": "",
              "childFareBasis": "",
              "codeShare": false,
              "connection": false,
              "departureAirport": "KIX",
              "departureTerminal": "",
              "departureTime": "201909231935",
              "departureTimeWithOffset": "",
              "duration": 105,
              "fareBasis": "NKX7ISJK",
              "fareType": "PRIVATE",
              "flightNumber": "KE740",
              "flyTime": 0,
              "key": "",
              "mainSegment": false,
              "marriageGrp": "",
              "operatingCarrier": "KE",
              "operatingFlightNumber": "KE740",
              "seats": 1,
              "status": "",
              "stopCity": [],
              "stopInfo": 0
            }
          ],
          "segmentSplicing": true
        }
      ],
      "itinerarySplicing": false,
      "masterCurrency": "CNY",
      "multiTicket": false,
      "nationalType": 0,
      "nationality": "",
      "onlineCheckIn": false,
      "oriAdultPrice": 400,
      "oriAdultTax": 0,
      "oriChildPrice": 400,
      "oriChildTax": 0,
      "oriInfantPrice": 0,
      "oriInfantTax": 0,
      "policyPriceChanges": [
        {
          "adultChange": {
            "absChange": {
              "amount": 4,
              "currency": "USD"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 0
            },
            "totalChange": {
              "amount": -56,
              "currency": "CNY"
            }
          },
          "childChange": {
            "absChange": {
              "amount": 4,
              "currency": "USD"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 0
            },
            "totalChange": {
              "amount": -56,
              "currency": "CNY"
            }
          },
          "displayNumber": "IC1908021687",
          "infantChange": null,
          "isFeeApplyToProvider": true,
          "otherAbsChangeDetails": [
            {
              "absTotal": {
                "amount": 10,
                "currency": "USD"
              },
              "desc": "INCENTIVE_RECEIVABLE",
              "totalChange": {
                "amount": 70,
                "currency": "CNY"
              }
            }
          ],
          "otherPercentageChangeDetails": [],
          "policyDesc": "IncentivePolicy:IC1908021687",
          "policyId": "5d4411fa73e1340001e3e890",
          "policyType": "INCENTIVE"
        },
        {
          "adultChange": {
            "absChange": {
              "amount": 5,
              "currency": "CNY"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 5.99
            },
            "totalChange": {
              "amount": 203.02872460376557,
              "currency": "CNY"
            }
          },
          "childChange": {
            "absChange": {
              "amount": 5,
              "currency": "CNY"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 5.99
            },
            "totalChange": {
              "amount": 203.02872460376557,
              "currency": "CNY"
            }
          },
          "displayNumber": "PF1907210860",
          "infantChange": {
            "absChange": {
              "amount": 5,
              "currency": "CNY"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 5.99
            },
            "totalChange": {
              "amount": 5.318583129454313,
              "currency": "CNY"
            }
          },
          "isFeeApplyToProvider": true,
          "otherAbsChangeDetails": [],
          "otherPercentageChangeDetails": [],
          "policyDesc": "PlatformPolicy:PF1907210860",
          "policyId": "5d342d9bf24d1c0001195a24",
          "policyType": "PLATFORM"
        }
      ],
      "posLocation": "CN",
      "priceType": 0,
      "providerCurrency": "EUR",
      "providerName": "skypk",
      "providerType": "PROVIDER_API",
      "routingId": "",
      "rule": {
        "changeBeforeDep": 0,
        "changeBeforeDepFee": 0,
        "changeDetail": null,
        "cnRemark": "",
        "currency": "CNY",
        "enRemark": "",
        "manualFareRule": null,
        "miniRule": -404,
        "noShowChange": 0,
        "noShowChangeAfter": 0,
        "noShowChangeAfterFee": 0,
        "noShowChangeFee": 0,
        "noShowRefund": 0,
        "noShowRefundAfter": 0,
        "noShowRefundAfterFee": 0,
        "noShowRefundFee": 0,
        "originRuleFee": {
          "changeAfterFee": -404,
          "changeAfterNoshowFee": -404,
          "changeBeforeFee": -404,
          "changeBeforeNoshowFee": -404,
          "currency": "",
          "refundAfterFee": -404,
          "refundAfterNoshowFee": -404,
          "refundBeforeFee": -404,
          "refundBeforeNoshowFee": -404
        },
        "partEndorse": 0,
        "partEndorsePrice": 0,
        "partRefund": 0,
        "partRefundFee": 0,
        "refundBeforeDep": 0,
        "refundBeforeDepFee": 0,
        "ruleFromOta": -404,
        "useOld": false
      },
      "saleBaggage": true,
      "seats": 1,
      "suitAge": "",
      "ticketInvoiceType": 0,
      "ticketPrice": 0,
      "ticketSource": 0,
      "ticketTimeLimitMinutes": 2880,
      "tof": "",
      "traceSpans": [
        {
          "application": "night-king",
          "createdAt": "2019-08-23T00:51:25.204127160Z",
          "desc": "move amount of 1.000000 from fare price to adult tax",
          "spanId": "4306392d-f399-4f71-9879-668974da1be6",
          "tags": {},
          "traceType": "None"
        },
        {
          "application": "night-king",
          "createdAt": "2019-08-23T00:51:25.204130459Z",
          "desc": "move amount of 1.000000 from child fare price to child tax",
          "spanId": "a4ea37d7-69d0-41e9-8665-d01f083b40ef",
          "tags": {},
          "traceType": "None"
        }
      ],
      "validSegmentsCount": 2,
      "validatingCarrier": "MM",
      "viewPrice": 0
    },
    {
      "accountCode": "",
      "aduTag": "",
      "adultPrice": 3313.389320285076,
      "adultPublishPrice": 3166.8574,
      "adultPublishTax": 0,
      "adultTax": 1,
      "adultTaxType": 0,
      "adultType": "",
      "adultUoTax": 0,
      "adultYqTax": 0,
      "adultYrTax": 0,
      "applyType": 0,
      "arf": "",
      "bookingToken": "AV3lIMEyBs_fUTSG1ptQEdHhNuiU41qiZIsqZP-3WXPjsPtnL7QYGnGsLJL3Rq8LXZ2JDTKrDsnUxGFyUIMcMyfE_mAvljAc06PaE7fvTdYaPUk_CL0g05XGbeEPzYNGi-HFOkuucoK7gYcg2lw_zygpjCvWuimoAYgyYa9Vq9MvQ1qB_v_KIAT7Kwij2dHQ6SmzXUZQr973EXgBpRWkGFtEJk80dwKlv7w4Jyuf360v8eRq-w3wnGJgJFKfXlJr8d5YIwF2ZP9EvfeUl5TMpTwO_MfOu266apXdsNLZPOXYS-0LHVWqV2s8tZWA3IrWvjCUblY3dkEq2yDsdLfF4liIPI3XWY3fLamNBsOQ2THNOsyN_nGc8QxClcEgepeVQkfzpvfPRKHwLhZom2dJDiz42Wh2lIjqUjk_Lz2TfVl5P8xnF9Wyjl63Hh7szcGQTg8YLka0_Phft0B-O0TnIkOoyJLD_IUyM2-EPAGDyzMYdb_o5gVu76bxSfl4mgfW_SJ23GEGpKBUmCJ46SrGXZg==",
      "cabin": "E",
      "chiTag": "",
      "childFareBasis": "",
      "childPrice": 3313.389320285076,
      "childPublishPrice": 3166.8574,
      "childPublishTax": 0,
      "childTax": 1,
      "childTaxType": 0,
      "childTicketPrice": 0,
      "childType": "",
      "childUoTax": 0,
      "childYqTax": 0,
      "childYrTax": 0,
      "ctof": "",
      "currency": "CNY",
      "currencyConversions": [
        {
          "from": "EUR",
          "rate": 7.8974,
          "source": "BOC",
          "timestamp": "2019-08-23T00:37:25Z",
          "to": "CNY"
        },
        {
          "from": "USD",
          "rate": 7,
          "source": "MANUAL",
          "timestamp": "2019-08-14T07:46:00Z",
          "to": "CNY"
        }
      ],
      "data": "99b6660f-ac71-4a10-8745-dcc9b4cf1e76#f33e73b8-3f05-4684-994a-3928d1d00ffe#KA872_E_ZE872_E",
      "eligibility": "",
      "evictionMarks": [
        {
          "evictionReason": "Platform[去哪人商旅] 航程内拼接",
          "traceSpans": [
            {
              "application": "night-king",
              "createdAt": null,
              "desc": "PlatformConfig filter",
              "spanId": "",
              "tags": {
                "DisplayNumber": "PFC1907306359",
                "Revision": "5"
              },
              "traceType": "None"
            }
          ]
        }
      ],
      "fareBasis": "",
      "fareCalcLine": "",
      "fareType": "PRIVATE",
      "flightCode": "",
      "infantPrice": 0,
      "infantPublishPrice": 0,
      "infantPublishTax": 0,
      "infantTax": 0,
      "infantTaxType": 0,
      "infantType": "",
      "itinerary": [
        {
          "destinationCity": "SEL",
          "duration": 27000,
          "originCity": "HKG",
          "segment": [
            {
              "accountCode": "",
              "aircraftCode": "320",
              "arrivalAirport": "PVG",
              "arrivalTerminal": "",
              "arrivalTime": "201909232045",
              "arrivalTimeWithOffset": "",
              "availabilitySource": "",
              "baggage": {
                "baggageCheck": false,
                "freeBaggagePiece": -1,
                "freeBaggageWeight": 15
              },
              "bookingClass": "N",
              "cabin": "E",
              "carrier": "KA",
              "childCabin": "",
              "childFareBasis": "",
              "codeShare": false,
              "connection": false,
              "departureAirport": "HKG",
              "departureTerminal": "",
              "departureTime": "201909231800",
              "departureTimeWithOffset": "",
              "duration": 165,
              "fareBasis": "QLXRRWE8",
              "fareType": "PRIVATE",
              "flightNumber": "KA872",
              "flyTime": 0,
              "key": "",
              "mainSegment": true,
              "marriageGrp": "",
              "operatingCarrier": "KA",
              "operatingFlightNumber": "KA872",
              "seats": 1,
              "status": "",
              "stopCity": [],
              "stopInfo": 0
            },
            {
              "accountCode": "",
              "aircraftCode": "",
              "arrivalAirport": "ICN",
              "arrivalTerminal": "",
              "arrivalTime": "201909240230",
              "arrivalTimeWithOffset": "",
              "availabilitySource": "",
              "baggage": {
                "baggageCheck": true,
                "freeBaggagePiece": -1,
                "freeBaggageWeight": 15
              },
              "bookingClass": "G",
              "cabin": "E",
              "carrier": "ZE",
              "childCabin": "",
              "childFareBasis": "",
              "codeShare": false,
              "connection": false,
              "departureAirport": "PVG",
              "departureTerminal": "",
              "departureTime": "201909232330",
              "departureTimeWithOffset": "",
              "duration": 120,
              "fareBasis": "ZOW",
              "fareType": "PRIVATE",
              "flightNumber": "ZE872",
              "flyTime": 0,
              "key": "",
              "mainSegment": false,
              "marriageGrp": "",
              "operatingCarrier": "",
              "operatingFlightNumber": "",
              "seats": 1,
              "status": "",
              "stopCity": [],
              "stopInfo": 0
            }
          ],
          "segmentSplicing": true
        }
      ],
      "itinerarySplicing": false,
      "masterCurrency": "CNY",
      "multiTicket": false,
      "nationalType": 0,
      "nationality": "",
      "onlineCheckIn": true,
      "oriAdultPrice": 401,
      "oriAdultTax": 0,
      "oriChildPrice": 401,
      "oriChildTax": 0,
      "oriInfantPrice": 0,
      "oriInfantTax": 0,
      "policyPriceChanges": [
        {
          "adultChange": {
            "absChange": {
              "amount": 4,
              "currency": "USD"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 0
            },
            "totalChange": {
              "amount": -56,
              "currency": "CNY"
            }
          },
          "childChange": {
            "absChange": {
              "amount": 4,
              "currency": "USD"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 0
            },
            "totalChange": {
              "amount": -56,
              "currency": "CNY"
            }
          },
          "displayNumber": "IC1908021687",
          "infantChange": null,
          "isFeeApplyToProvider": true,
          "otherAbsChangeDetails": [
            {
              "absTotal": {
                "amount": 10,
                "currency": "USD"
              },
              "desc": "INCENTIVE_RECEIVABLE",
              "totalChange": {
                "amount": 70,
                "currency": "CNY"
              }
            }
          ],
          "otherPercentageChangeDetails": [],
          "policyDesc": "IncentivePolicy:IC1908021687",
          "policyId": "5d4411fa73e1340001e3e890",
          "policyType": "INCENTIVE"
        },
        {
          "adultChange": {
            "absChange": {
              "amount": 5,
              "currency": "CNY"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 5.99
            },
            "totalChange": {
              "amount": 203.53192028507604,
              "currency": "CNY"
            }
          },
          "childChange": {
            "absChange": {
              "amount": 5,
              "currency": "CNY"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 5.99
            },
            "totalChange": {
              "amount": 203.53192028507604,
              "currency": "CNY"
            }
          },
          "displayNumber": "PF1907210860",
          "infantChange": {
            "absChange": {
              "amount": 5,
              "currency": "CNY"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 5.99
            },
            "totalChange": {
              "amount": 5.318583129454313,
              "currency": "CNY"
            }
          },
          "isFeeApplyToProvider": true,
          "otherAbsChangeDetails": [],
          "otherPercentageChangeDetails": [],
          "policyDesc": "PlatformPolicy:PF1907210860",
          "policyId": "5d342d9bf24d1c0001195a24",
          "policyType": "PLATFORM"
        }
      ],
      "posLocation": "CN",
      "priceType": 0,
      "providerCurrency": "EUR",
      "providerName": "skypk",
      "providerType": "PROVIDER_API",
      "routingId": "",
      "rule": {
        "changeBeforeDep": 0,
        "changeBeforeDepFee": 0,
        "changeDetail": null,
        "cnRemark": "",
        "currency": "CNY",
        "enRemark": "",
        "manualFareRule": null,
        "miniRule": -404,
        "noShowChange": 0,
        "noShowChangeAfter": 0,
        "noShowChangeAfterFee": 0,
        "noShowChangeFee": 0,
        "noShowRefund": 0,
        "noShowRefundAfter": 0,
        "noShowRefundAfterFee": 0,
        "noShowRefundFee": 0,
        "originRuleFee": {
          "changeAfterFee": -404,
          "changeAfterNoshowFee": -404,
          "changeBeforeFee": -404,
          "changeBeforeNoshowFee": -404,
          "currency": "",
          "refundAfterFee": -404,
          "refundAfterNoshowFee": -404,
          "refundBeforeFee": -404,
          "refundBeforeNoshowFee": -404
        },
        "partEndorse": 0,
        "partEndorsePrice": 0,
        "partRefund": 0,
        "partRefundFee": 0,
        "refundBeforeDep": 0,
        "refundBeforeDepFee": 0,
        "ruleFromOta": -404,
        "useOld": false
      },
      "saleBaggage": false,
      "seats": 1,
      "suitAge": "",
      "ticketInvoiceType": 0,
      "ticketPrice": 0,
      "ticketSource": 0,
      "ticketTimeLimitMinutes": 2880,
      "tof": "",
      "traceSpans": [
        {
          "application": "night-king",
          "createdAt": "2019-08-23T00:51:25.204172346Z",
          "desc": "move amount of 1.000000 from fare price to adult tax",
          "spanId": "75ba62cf-1b00-4e76-86cb-616457f5ff83",
          "tags": {},
          "traceType": "None"
        },
        {
          "application": "night-king",
          "createdAt": "2019-08-23T00:51:25.204175526Z",
          "desc": "move amount of 1.000000 from child fare price to child tax",
          "spanId": "8fa3542b-256c-409a-8833-6d9d508c67eb",
          "tags": {},
          "traceType": "None"
        }
      ],
      "validSegmentsCount": 2,
      "validatingCarrier": "KA",
      "viewPrice": 0
    },
    {
      "accountCode": "",
      "aduTag": "",
      "adultPrice": 3321.7899159663866,
      "adultPublishPrice": 3174.7548,
      "adultPublishTax": 0,
      "adultTax": 1,
      "adultTaxType": 0,
      "adultType": "",
      "adultUoTax": 0,
      "adultYqTax": 0,
      "adultYrTax": 0,
      "applyType": 0,
      "arf": "",
      "bookingToken": "AtHQzzR13z9nzY5o3dR01DHnrdM6MT2KisJi7UQBDmdlhvThw-S1OPMfpQaQ45BwWi-U92oxXxB08o4Dw8CHx_EsK_RJXQh7e9Soto129faQ4Yx-cd_ei3zV5yQ-GO2hmTaEwOGTPGIoV1c5Hqtd62rnbenRLDZfZPb1TkGWPMqLop8bXWq8irj_fmhmd3f3kClGxwS5BFok6fCXvG7v82rjBqSA165J7hq2MZEDufJ4o38W-j_DmoONIvBwTwJnqDIZT8LaVltVATW5UPD9oTe6gZlgeaO0LGqlB2FfNU_NNEVyvbUTjilhzLnIzguVwaIOuEpjm3LaNnOXPr9y8SjY4iWpqENZ7NOA17yacg9ZTKsIuNNH3oIktmmURLFBY7D_6NdqHoASohLsFrF3mXFZQ3QSdoZIGwrumiXsCvSQ0szWXKdWUiakyq5XE6w5aOiQc220rb2Fst-fJ3kjis30elMDFXm6GBF5VVe91aDwTuV9bFTr_E-8zvu4uCwKwnhUcRTNbOwDHJq3KZnGKeQ==",
      "cabin": "E",
      "chiTag": "",
      "childFareBasis": "",
      "childPrice": 3321.7899159663866,
      "childPublishPrice": 3174.7548,
      "childPublishTax": 0,
      "childTax": 1,
      "childTaxType": 0,
      "childTicketPrice": 0,
      "childType": "",
      "childUoTax": 0,
      "childYqTax": 0,
      "childYrTax": 0,
      "ctof": "",
      "currency": "CNY",
      "currencyConversions": [
        {
          "from": "EUR",
          "rate": 7.8974,
          "source": "BOC",
          "timestamp": "2019-08-23T00:37:25Z",
          "to": "CNY"
        },
        {
          "from": "USD",
          "rate": 7,
          "source": "MANUAL",
          "timestamp": "2019-08-14T07:46:00Z",
          "to": "CNY"
        }
      ],
      "data": "99b6660f-ac71-4a10-8745-dcc9b4cf1e76#9cac4563-2432-49d5-852b-032619e0e830#GK20_E_KE706_E",
      "eligibility": "",
      "evictionMarks": [
        {
          "evictionReason": "Platform[去哪人商旅] 航程内拼接",
          "traceSpans": [
            {
              "application": "night-king",
              "createdAt": null,
              "desc": "PlatformConfig filter",
              "spanId": "",
              "tags": {
                "DisplayNumber": "PFC1907306359",
                "Revision": "5"
              },
              "traceType": "None"
            }
          ]
        }
      ],
      "fareBasis": "",
      "fareCalcLine": "",
      "fareType": "PRIVATE",
      "flightCode": "",
      "infantPrice": 0,
      "infantPublishPrice": 0,
      "infantPublishTax": 0,
      "infantTax": 0,
      "infantTaxType": 0,
      "infantType": "",
      "itinerary": [
        {
          "destinationCity": "SEL",
          "duration": 33000,
          "originCity": "HKG",
          "segment": [
            {
              "accountCode": "",
              "aircraftCode": "",
              "arrivalAirport": "NRT",
              "arrivalTerminal": "",
              "arrivalTime": "201909230710",
              "arrivalTimeWithOffset": "",
              "availabilitySource": "",
              "baggage": {
                "baggageCheck": false,
                "freeBaggagePiece": -1,
                "freeBaggageWeight": 0
              },
              "bookingClass": "S",
              "cabin": "E",
              "carrier": "GK",
              "childCabin": "",
              "childFareBasis": "",
              "codeShare": false,
              "connection": false,
              "departureAirport": "HKG",
              "departureTerminal": "",
              "departureTime": "201909230135",
              "departureTimeWithOffset": "",
              "duration": 275,
              "fareBasis": "ELECOE1",
              "fareType": "PRIVATE",
              "flightNumber": "GK20",
              "flyTime": 0,
              "key": "",
              "mainSegment": true,
              "marriageGrp": "",
              "operatingCarrier": "",
              "operatingFlightNumber": "",
              "seats": 1,
              "status": "",
              "stopCity": [],
              "stopInfo": 0
            },
            {
              "accountCode": "",
              "aircraftCode": "772",
              "arrivalAirport": "ICN",
              "arrivalTerminal": "",
              "arrivalTime": "201909231145",
              "arrivalTimeWithOffset": "",
              "availabilitySource": "",
              "baggage": {
                "baggageCheck": true,
                "freeBaggagePiece": -1,
                "freeBaggageWeight": 0
              },
              "bookingClass": "N",
              "cabin": "E",
              "carrier": "KE",
              "childCabin": "",
              "childFareBasis": "",
              "codeShare": false,
              "connection": false,
              "departureAirport": "NRT",
              "departureTerminal": "",
              "departureTime": "201909230915",
              "departureTimeWithOffset": "",
              "duration": 150,
              "fareBasis": "NKX3ISJN",
              "fareType": "PRIVATE",
              "flightNumber": "KE706",
              "flyTime": 0,
              "key": "",
              "mainSegment": false,
              "marriageGrp": "",
              "operatingCarrier": "KE",
              "operatingFlightNumber": "KE706",
              "seats": 1,
              "status": "",
              "stopCity": [],
              "stopInfo": 0
            }
          ],
          "segmentSplicing": true
        }
      ],
      "itinerarySplicing": false,
      "masterCurrency": "CNY",
      "multiTicket": false,
      "nationalType": 0,
      "nationality": "",
      "onlineCheckIn": false,
      "oriAdultPrice": 402,
      "oriAdultTax": 0,
      "oriChildPrice": 402,
      "oriChildTax": 0,
      "oriInfantPrice": 0,
      "oriInfantTax": 0,
      "policyPriceChanges": [
        {
          "adultChange": {
            "absChange": {
              "amount": 4,
              "currency": "USD"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 0
            },
            "totalChange": {
              "amount": -56,
              "currency": "CNY"
            }
          },
          "childChange": {
            "absChange": {
              "amount": 4,
              "currency": "USD"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 0
            },
            "totalChange": {
              "amount": -56,
              "currency": "CNY"
            }
          },
          "displayNumber": "IC1908021687",
          "infantChange": null,
          "isFeeApplyToProvider": true,
          "otherAbsChangeDetails": [
            {
              "absTotal": {
                "amount": 10,
                "currency": "USD"
              },
              "desc": "INCENTIVE_RECEIVABLE",
              "totalChange": {
                "amount": 70,
                "currency": "CNY"
              }
            }
          ],
          "otherPercentageChangeDetails": [],
          "policyDesc": "IncentivePolicy:IC1908021687",
          "policyId": "5d4411fa73e1340001e3e890",
          "policyType": "INCENTIVE"
        },
        {
          "adultChange": {
            "absChange": {
              "amount": 5,
              "currency": "CNY"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 5.99
            },
            "totalChange": {
              "amount": 204.03511596638657,
              "currency": "CNY"
            }
          },
          "childChange": {
            "absChange": {
              "amount": 5,
              "currency": "CNY"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 5.99
            },
            "totalChange": {
              "amount": 204.03511596638657,
              "currency": "CNY"
            }
          },
          "displayNumber": "PF1907210860",
          "infantChange": {
            "absChange": {
              "amount": 5,
              "currency": "CNY"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 5.99
            },
            "totalChange": {
              "amount": 5.318583129454313,
              "currency": "CNY"
            }
          },
          "isFeeApplyToProvider": true,
          "otherAbsChangeDetails": [],
          "otherPercentageChangeDetails": [],
          "policyDesc": "PlatformPolicy:PF1907210860",
          "policyId": "5d342d9bf24d1c0001195a24",
          "policyType": "PLATFORM"
        }
      ],
      "posLocation": "CN",
      "priceType": 0,
      "providerCurrency": "EUR",
      "providerName": "skypk",
      "providerType": "PROVIDER_API",
      "routingId": "",
      "rule": {
        "changeBeforeDep": 0,
        "changeBeforeDepFee": 0,
        "changeDetail": null,
        "cnRemark": "",
        "currency": "CNY",
        "enRemark": "",
        "manualFareRule": null,
        "miniRule": -404,
        "noShowChange": 0,
        "noShowChangeAfter": 0,
        "noShowChangeAfterFee": 0,
        "noShowChangeFee": 0,
        "noShowRefund": 0,
        "noShowRefundAfter": 0,
        "noShowRefundAfterFee": 0,
        "noShowRefundFee": 0,
        "originRuleFee": {
          "changeAfterFee": -404,
          "changeAfterNoshowFee": -404,
          "changeBeforeFee": -404,
          "changeBeforeNoshowFee": -404,
          "currency": "",
          "refundAfterFee": -404,
          "refundAfterNoshowFee": -404,
          "refundBeforeFee": -404,
          "refundBeforeNoshowFee": -404
        },
        "partEndorse": 0,
        "partEndorsePrice": 0,
        "partRefund": 0,
        "partRefundFee": 0,
        "refundBeforeDep": 0,
        "refundBeforeDepFee": 0,
        "ruleFromOta": -404,
        "useOld": false
      },
      "saleBaggage": true,
      "seats": 1,
      "suitAge": "",
      "ticketInvoiceType": 0,
      "ticketPrice": 0,
      "ticketSource": 0,
      "ticketTimeLimitMinutes": 2880,
      "tof": "",
      "traceSpans": [
        {
          "application": "night-king",
          "createdAt": "2019-08-23T00:51:25.204221224Z",
          "desc": "move amount of 1.000000 from fare price to adult tax",
          "spanId": "f2d644c8-db2c-48dd-ac45-bf280cad1b18",
          "tags": {},
          "traceType": "None"
        },
        {
          "application": "night-king",
          "createdAt": "2019-08-23T00:51:25.204224462Z",
          "desc": "move amount of 1.000000 from child fare price to child tax",
          "spanId": "9b94f0c4-392c-48e8-a041-3b09ce63addf",
          "tags": {},
          "traceType": "None"
        }
      ],
      "validSegmentsCount": 2,
      "validatingCarrier": "GK",
      "viewPrice": 0
    },
    {
      "accountCode": "",
      "aduTag": "",
      "adultPrice": 4116.028188490586,
      "adultPublishPrice": 3893.4182,
      "adultPublishTax": 0,
      "adultTax": 1,
      "adultTaxType": 0,
      "adultType": "",
      "adultUoTax": 0,
      "adultYqTax": 0,
      "adultYrTax": 0,
      "applyType": 0,
      "arf": "",
      "bookingToken": "AIK1Ttx0GU0PQNrRm9AjjbUFlV3u-me06Sjw5zj8GqgowXp-aiADZJX0nGv0rWTpomBeMJQjk4M385vD3Kvf7R6Iw302votXcLuZ5y8M3K8tLJ_YKj5AVRDKA5Qva77qk0jsg4Q1fjjpsjuVKCXBL_l0mY8kXDbdc72gg13I4bt9cYxhJTH2WDtQov0NnZBmADg2tVN8kK4zh4ujpToZ5zB-HG91l6ETcSjyHxrW4jJLIHyNDBMcbq5iYuQMOOw_XUhpSAGHY7glrL82RSwNpIVCAFiSq4w9_WoT9Cf_nDjJtuuhY-u3a9jT2y0-jujgcIRJ9rCuThBlcuHeriXo8gEfg8BnTjAPtEefEwVKmpN3mJ-2t98Xos-asTo16oY8VQuNiBCzwOnC7QOG7mFP9oRl7wwAM1cB7lmUtfnD8U61HRUJhYDOoTjZ4KMQ7-Dm_x4K6EoYzk7iOFhWgV5M2kBgD1Zo3NWfxCEHPW_Te2cw=",
      "cabin": "E",
      "chiTag": "",
      "childFareBasis": "",
      "childPrice": 4116.028188490586,
      "childPublishPrice": 3893.4182,
      "childPublishTax": 0,
      "childTax": 1,
      "childTaxType": 0,
      "childTicketPrice": 0,
      "childType": "",
      "childUoTax": 0,
      "childYqTax": 0,
      "childYrTax": 0,
      "ctof": "",
      "currency": "CNY",
      "currencyConversions": [
        {
          "from": "EUR",
          "rate": 7.8974,
          "source": "BOC",
          "timestamp": "2019-08-23T00:37:25Z",
          "to": "CNY"
        },
        {
          "from": "USD",
          "rate": 7,
          "source": "MANUAL",
          "timestamp": "2019-08-14T07:46:00Z",
          "to": "CNY"
        }
      ],
      "data": "99b6660f-ac71-4a10-8745-dcc9b4cf1e76#068873b3-806e-4df8-bc5b-bb201d42c2ff#CX412_E",
      "eligibility": "",
      "evictionMarks": [
        {
          "evictionReason": "Platform[去哪人商旅] 航程内拼接",
          "traceSpans": [
            {
              "application": "night-king",
              "createdAt": null,
              "desc": "PlatformConfig filter",
              "spanId": "",
              "tags": {
                "DisplayNumber": "PFC1907306359",
                "Revision": "5"
              },
              "traceType": "None"
            }
          ]
        }
      ],
      "fareBasis": "",
      "fareCalcLine": "",
      "fareType": "PRIVATE",
      "flightCode": "",
      "infantPrice": 0,
      "infantPublishPrice": 0,
      "infantPublishTax": 0,
      "infantTax": 0,
      "infantTaxType": 0,
      "infantType": "",
      "itinerary": [
        {
          "destinationCity": "SEL",
          "duration": 13800,
          "originCity": "HKG",
          "segment": [
            {
              "accountCode": "",
              "aircraftCode": "333",
              "arrivalAirport": "ICN",
              "arrivalTerminal": "",
              "arrivalTime": "201909230555",
              "arrivalTimeWithOffset": "",
              "availabilitySource": "",
              "baggage": {
                "baggageCheck": false,
                "freeBaggagePiece": -1,
                "freeBaggageWeight": 20
              },
              "bookingClass": "Q",
              "cabin": "E",
              "carrier": "CX",
              "childCabin": "",
              "childFareBasis": "",
              "codeShare": false,
              "connection": false,
              "departureAirport": "HKG",
              "departureTerminal": "",
              "departureTime": "201909230105",
              "departureTimeWithOffset": "",
              "duration": 230,
              "fareBasis": "SLARRWG8",
              "fareType": "PRIVATE",
              "flightNumber": "CX412",
              "flyTime": 0,
              "key": "",
              "mainSegment": true,
              "marriageGrp": "",
              "operatingCarrier": "CX",
              "operatingFlightNumber": "CX412",
              "seats": 1,
              "status": "",
              "stopCity": [],
              "stopInfo": 0
            }
          ],
          "segmentSplicing": true
        }
      ],
      "itinerarySplicing": false,
      "masterCurrency": "CNY",
      "multiTicket": false,
      "nationalType": 0,
      "nationality": "",
      "onlineCheckIn": true,
      "oriAdultPrice": 493,
      "oriAdultTax": 0,
      "oriChildPrice": 493,
      "oriChildTax": 0,
      "oriInfantPrice": 0,
      "oriInfantTax": 0,
      "policyPriceChanges": [
        {
          "adultChange": {
            "absChange": {
              "amount": 4,
              "currency": "USD"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 0
            },
            "totalChange": {
              "amount": -28,
              "currency": "CNY"
            }
          },
          "childChange": {
            "absChange": {
              "amount": 4,
              "currency": "USD"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 0
            },
            "totalChange": {
              "amount": -28,
              "currency": "CNY"
            }
          },
          "displayNumber": "IC1908021687",
          "infantChange": null,
          "isFeeApplyToProvider": true,
          "otherAbsChangeDetails": [
            {
              "absTotal": {
                "amount": 5,
                "currency": "USD"
              },
              "desc": "INCENTIVE_RECEIVABLE",
              "totalChange": {
                "amount": 35,
                "currency": "CNY"
              }
            }
          ],
          "otherPercentageChangeDetails": [],
          "policyDesc": "IncentivePolicy:IC1908021687",
          "policyId": "5d4411fa73e1340001e3e890",
          "policyType": "INCENTIVE"
        },
        {
          "adultChange": {
            "absChange": {
              "amount": 5,
              "currency": "CNY"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 5.99
            },
            "totalChange": {
              "amount": 251.60998849058612,
              "currency": "CNY"
            }
          },
          "childChange": {
            "absChange": {
              "amount": 5,
              "currency": "CNY"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 5.99
            },
            "totalChange": {
              "amount": 251.60998849058612,
              "currency": "CNY"
            }
          },
          "displayNumber": "PF1907210860",
          "infantChange": {
            "absChange": {
              "amount": 5,
              "currency": "CNY"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 5.99
            },
            "totalChange": {
              "amount": 5.318583129454313,
              "currency": "CNY"
            }
          },
          "isFeeApplyToProvider": true,
          "otherAbsChangeDetails": [],
          "otherPercentageChangeDetails": [],
          "policyDesc": "PlatformPolicy:PF1907210860",
          "policyId": "5d342d9bf24d1c0001195a24",
          "policyType": "PLATFORM"
        }
      ],
      "posLocation": "CN",
      "priceType": 0,
      "providerCurrency": "EUR",
      "providerName": "skypk",
      "providerType": "PROVIDER_API",
      "routingId": "",
      "rule": {
        "changeBeforeDep": 0,
        "changeBeforeDepFee": 0,
        "changeDetail": null,
        "cnRemark": "",
        "currency": "CNY",
        "enRemark": "",
        "manualFareRule": null,
        "miniRule": -404,
        "noShowChange": 0,
        "noShowChangeAfter": 0,
        "noShowChangeAfterFee": 0,
        "noShowChangeFee": 0,
        "noShowRefund": 0,
        "noShowRefundAfter": 0,
        "noShowRefundAfterFee": 0,
        "noShowRefundFee": 0,
        "originRuleFee": {
          "changeAfterFee": -404,
          "changeAfterNoshowFee": -404,
          "changeBeforeFee": -404,
          "changeBeforeNoshowFee": -404,
          "currency": "",
          "refundAfterFee": -404,
          "refundAfterNoshowFee": -404,
          "refundBeforeFee": -404,
          "refundBeforeNoshowFee": -404
        },
        "partEndorse": 0,
        "partEndorsePrice": 0,
        "partRefund": 0,
        "partRefundFee": 0,
        "refundBeforeDep": 0,
        "refundBeforeDepFee": 0,
        "ruleFromOta": -404,
        "useOld": false
      },
      "saleBaggage": false,
      "seats": 1,
      "suitAge": "",
      "ticketInvoiceType": 0,
      "ticketPrice": 0,
      "ticketSource": 0,
      "ticketTimeLimitMinutes": 2880,
      "tof": "",
      "traceSpans": [
        {
          "application": "night-king",
          "createdAt": "2019-08-23T00:51:25.204265691Z",
          "desc": "move amount of 1.000000 from fare price to adult tax",
          "spanId": "b97cc0f9-0570-46bb-a1ff-f2485cb1bbcb",
          "tags": {},
          "traceType": "None"
        },
        {
          "application": "night-king",
          "createdAt": "2019-08-23T00:51:25.204268894Z",
          "desc": "move amount of 1.000000 from child fare price to child tax",
          "spanId": "ed921834-c821-472f-af1b-236d3a15fe4e",
          "tags": {},
          "traceType": "None"
        }
      ],
      "validSegmentsCount": 1,
      "validatingCarrier": "CX",
      "viewPrice": 0
    },
    {
      "accountCode": "",
      "aduTag": "",
      "adultPrice": 4123.664822891182,
      "adultPublishPrice": 3956.5974,
      "adultPublishTax": 0,
      "adultTax": 1,
      "adultTaxType": 0,
      "adultType": "",
      "adultUoTax": 0,
      "adultYqTax": 0,
      "adultYrTax": 0,
      "applyType": 0,
      "arf": "",
      "bookingToken": "AnT6jPusg0oPtyPMkfZWJLs7oqG8a8O6N7IQ7g0yuaqBZ5YR-SiQUAjh5KOODVHmFWBF1wI7OvWLe2NX9eDznUS7bUbXRqAakraiqaZogfzZM7ByTh7uN7j2G7W-3yKtny2NfXoWonCCHYc9w0yKhTeNbv8HQJ2W_cihj7RQ6ZUJI3sLI020S1yeulUT5I4DQ1pLQJqh6IsvgybqU7qe39vllQfui0rmDaGsBJxXQNu8f0hKiEqMPOpsFIPptF6XocrbECXiT38FsWl9XFS987psgNF5P2t3d-QvgwK6MltgA6hJwfyeNN1o9mKH_nZZ1rOlaEwOTkLui7SMkTTd1sVAwEGj6Ny1ZE99yqGkpl1GQT4ipmXwtEaKlowEZkcWF60EuUpwjUMs0SaszA5BcQltwViifC-2M9V2liH1pUudz70nWVE2FUpqxEysxd2DQHentYbqZ5a7cHWMoEzZkQD-IgsqXKD5SBI8clFArI4N6ZJgv-iSg-Sq4cJ6o2p26qc2ITupgteELz0kkZDGQWA==",
      "cabin": "E",
      "chiTag": "",
      "childFareBasis": "",
      "childPrice": 4123.664822891182,
      "childPublishPrice": 3956.5974,
      "childPublishTax": 0,
      "childTax": 1,
      "childTaxType": 0,
      "childTicketPrice": 0,
      "childType": "",
      "childUoTax": 0,
      "childYqTax": 0,
      "childYrTax": 0,
      "ctof": "",
      "currency": "CNY",
      "currencyConversions": [
        {
          "from": "EUR",
          "rate": 7.8974,
          "source": "BOC",
          "timestamp": "2019-08-23T00:37:25Z",
          "to": "CNY"
        },
        {
          "from": "USD",
          "rate": 7,
          "source": "MANUAL",
          "timestamp": "2019-08-14T07:46:00Z",
          "to": "CNY"
        }
      ],
      "data": "99b6660f-ac71-4a10-8745-dcc9b4cf1e76#cd031e17-a942-48e7-9eb5-4bd54fca574c#BR892_E_OZ9744_E_BX8824_E",
      "eligibility": "",
      "evictionMarks": [
        {
          "evictionReason": "Platform[去哪人商旅] 航程内拼接",
          "traceSpans": [
            {
              "application": "night-king",
              "createdAt": null,
              "desc": "PlatformConfig filter",
              "spanId": "",
              "tags": {
                "DisplayNumber": "PFC1907306359",
                "Revision": "5"
              },
              "traceType": "None"
            }
          ]
        }
      ],
      "fareBasis": "",
      "fareCalcLine": "",
      "fareType": "PRIVATE",
      "flightCode": "",
      "infantPrice": 0,
      "infantPublishPrice": 0,
      "infantPublishTax": 0,
      "infantTax": 0,
      "infantTaxType": 0,
      "infantType": "",
      "itinerary": [
        {
          "destinationCity": "SEL",
          "duration": 32700,
          "originCity": "HKG",
          "segment": [
            {
              "accountCode": "",
              "aircraftCode": "789",
              "arrivalAirport": "TPE",
              "arrivalTerminal": "",
              "arrivalTime": "201909231140",
              "arrivalTimeWithOffset": "",
              "availabilitySource": "",
              "baggage": {
                "baggageCheck": false,
                "freeBaggagePiece": -1,
                "freeBaggageWeight": 15
              },
              "bookingClass": "S",
              "cabin": "E",
              "carrier": "BR",
              "childCabin": "",
              "childFareBasis": "",
              "codeShare": false,
              "connection": false,
              "departureAirport": "HKG",
              "departureTerminal": "",
              "departureTime": "201909230950",
              "departureTimeWithOffset": "",
              "duration": 110,
              "fareBasis": "BLOWHK",
              "fareType": "PRIVATE",
              "flightNumber": "BR892",
              "flyTime": 0,
              "key": "",
              "mainSegment": false,
              "marriageGrp": "",
              "operatingCarrier": "BR",
              "operatingFlightNumber": "BR892",
              "seats": 1,
              "status": "",
              "stopCity": [],
              "stopInfo": 0
            },
            {
              "accountCode": "",
              "aircraftCode": "321",
              "arrivalAirport": "PUS",
              "arrivalTerminal": "",
              "arrivalTime": "201909231630",
              "arrivalTimeWithOffset": "",
              "availabilitySource": "",
              "baggage": {
                "baggageCheck": false,
                "freeBaggagePiece": -1,
                "freeBaggageWeight": 15
              },
              "bookingClass": "L",
              "cabin": "E",
              "carrier": "OZ",
              "childCabin": "",
              "childFareBasis": "",
              "codeShare": true,
              "connection": false,
              "departureAirport": "TPE",
              "departureTerminal": "",
              "departureTime": "201909231320",
              "departureTimeWithOffset": "",
              "duration": 130,
              "fareBasis": "ELOSKBX",
              "fareType": "PRIVATE",
              "flightNumber": "OZ9744",
              "flyTime": 0,
              "key": "",
              "mainSegment": true,
              "marriageGrp": "",
              "operatingCarrier": "BX",
              "operatingFlightNumber": "BX794",
              "seats": 1,
              "status": "",
              "stopCity": [],
              "stopInfo": 0
            },
            {
              "accountCode": "",
              "aircraftCode": "",
              "arrivalAirport": "GMP",
              "arrivalTerminal": "",
              "arrivalTime": "201909231955",
              "arrivalTimeWithOffset": "",
              "availabilitySource": "",
              "baggage": {
                "baggageCheck": true,
                "freeBaggagePiece": -1,
                "freeBaggageWeight": 15
              },
              "bookingClass": "G",
              "cabin": "E",
              "carrier": "BX",
              "childCabin": "",
              "childFareBasis": "",
              "codeShare": false,
              "connection": false,
              "departureAirport": "PUS",
              "departureTerminal": "",
              "departureTime": "201909231900",
              "departureTimeWithOffset": "",
              "duration": 55,
              "fareBasis": "",
              "fareType": "PRIVATE",
              "flightNumber": "BX8824",
              "flyTime": 0,
              "key": "",
              "mainSegment": false,
              "marriageGrp": "",
              "operatingCarrier": "",
              "operatingFlightNumber": "",
              "seats": 1,
              "status": "",
              "stopCity": [],
              "stopInfo": 0
            }
          ],
          "segmentSplicing": true
        }
      ],
      "itinerarySplicing": false,
      "masterCurrency": "CNY",
      "multiTicket": false,
      "nationalType": 0,
      "nationality": "",
      "onlineCheckIn": false,
      "oriAdultPrice": 501,
      "oriAdultTax": 0,
      "oriChildPrice": 501,
      "oriChildTax": 0,
      "oriInfantPrice": 0,
      "oriInfantTax": 0,
      "policyPriceChanges": [
        {
          "adultChange": {
            "absChange": {
              "amount": 4,
              "currency": "USD"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 0
            },
            "totalChange": {
              "amount": -84,
              "currency": "CNY"
            }
          },
          "childChange": {
            "absChange": {
              "amount": 4,
              "currency": "USD"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 0
            },
            "totalChange": {
              "amount": -84,
              "currency": "CNY"
            }
          },
          "displayNumber": "IC1908021687",
          "infantChange": null,
          "isFeeApplyToProvider": true,
          "otherAbsChangeDetails": [
            {
              "absTotal": {
                "amount": 15,
                "currency": "USD"
              },
              "desc": "INCENTIVE_RECEIVABLE",
              "totalChange": {
                "amount": 105,
                "currency": "CNY"
              }
            }
          ],
          "otherPercentageChangeDetails": [],
          "policyDesc": "IncentivePolicy:IC1908021687",
          "policyId": "5d4411fa73e1340001e3e890",
          "policyType": "INCENTIVE"
        },
        {
          "adultChange": {
            "absChange": {
              "amount": 5,
              "currency": "CNY"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 5.99
            },
            "totalChange": {
              "amount": 252.06742289118182,
              "currency": "CNY"
            }
          },
          "childChange": {
            "absChange": {
              "amount": 5,
              "currency": "CNY"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 5.99
            },
            "totalChange": {
              "amount": 252.06742289118182,
              "currency": "CNY"
            }
          },
          "displayNumber": "PF1907210860",
          "infantChange": {
            "absChange": {
              "amount": 5,
              "currency": "CNY"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 5.99
            },
            "totalChange": {
              "amount": 5.318583129454313,
              "currency": "CNY"
            }
          },
          "isFeeApplyToProvider": true,
          "otherAbsChangeDetails": [],
          "otherPercentageChangeDetails": [],
          "policyDesc": "PlatformPolicy:PF1907210860",
          "policyId": "5d342d9bf24d1c0001195a24",
          "policyType": "PLATFORM"
        }
      ],
      "posLocation": "CN",
      "priceType": 0,
      "providerCurrency": "EUR",
      "providerName": "skypk",
      "providerType": "PROVIDER_API",
      "routingId": "",
      "rule": {
        "changeBeforeDep": 0,
        "changeBeforeDepFee": 0,
        "changeDetail": null,
        "cnRemark": "",
        "currency": "CNY",
        "enRemark": "",
        "manualFareRule": null,
        "miniRule": -404,
        "noShowChange": 0,
        "noShowChangeAfter": 0,
        "noShowChangeAfterFee": 0,
        "noShowChangeFee": 0,
        "noShowRefund": 0,
        "noShowRefundAfter": 0,
        "noShowRefundAfterFee": 0,
        "noShowRefundFee": 0,
        "originRuleFee": {
          "changeAfterFee": -404,
          "changeAfterNoshowFee": -404,
          "changeBeforeFee": -404,
          "changeBeforeNoshowFee": -404,
          "currency": "",
          "refundAfterFee": -404,
          "refundAfterNoshowFee": -404,
          "refundBeforeFee": -404,
          "refundBeforeNoshowFee": -404
        },
        "partEndorse": 0,
        "partEndorsePrice": 0,
        "partRefund": 0,
        "partRefundFee": 0,
        "refundBeforeDep": 0,
        "refundBeforeDepFee": 0,
        "ruleFromOta": -404,
        "useOld": false
      },
      "saleBaggage": false,
      "seats": 1,
      "suitAge": "",
      "ticketInvoiceType": 0,
      "ticketPrice": 0,
      "ticketSource": 0,
      "ticketTimeLimitMinutes": 2880,
      "tof": "",
      "traceSpans": [
        {
          "application": "night-king",
          "createdAt": "2019-08-23T00:51:25.204589850Z",
          "desc": "move amount of 1.000000 from fare price to adult tax",
          "spanId": "42fef377-c4ef-4da3-aed7-36b479fc3371",
          "tags": {},
          "traceType": "None"
        },
        {
          "application": "night-king",
          "createdAt": "2019-08-23T00:51:25.204592891Z",
          "desc": "move amount of 1.000000 from child fare price to child tax",
          "spanId": "ac89b7ad-5e4a-4434-84ba-c0deb376bb92",
          "tags": {},
          "traceType": "None"
        }
      ],
      "validSegmentsCount": 3,
      "validatingCarrier": "BR",
      "viewPrice": 0
    },
    {
      "accountCode": "",
      "aduTag": "",
      "adultPrice": 4216.071375385597,
      "adultPublishPrice": 4043.4688,
      "adultPublishTax": 0,
      "adultTax": 1,
      "adultTaxType": 0,
      "adultType": "",
      "adultUoTax": 0,
      "adultYqTax": 0,
      "adultYrTax": 0,
      "applyType": 0,
      "arf": "",
      "bookingToken": "AP6lzLUJCbDUqADCG1bRelkm0dCmujgBDbi-cK7ZzFDplBPuFGjFiK1sPF1bJZa4hFN7uFFM50ZZiPFAVZSC3ck86PgappqysqmkhlA1-ueQy29ypRvnfUQq00PxY53nBa5NT9txmop7SYTQfsn7TfeRcJHP0MosZHsQ5G4Lyej5BibsHshN4hYBqBXadhzQ0SHNdI-53F4tWfEA732Ho5gJnxar6RdH9ZCuurEATljUzORpgC3HMyAfvgMDQbxxBGyJP3BPgcty5NRrux9CAYroaOTV6F5up0lNriwPi7eMbehQYc0HkUqdomDyPHf6QWewrUgs03X-6kSuNoC-YGAh9uH_NiQR8r4JwUfVQs24O4-a1GeX_9nBH0PLmnjZiQ_ux8Dzwi8E0ft6ilDLZRXLL2itVKjhMdlvyeIVa7TdgSpt9deHygA3ss5WtFN6kTcguyBl2nZVGMb6FwLFhgeYrFIRLS6bU3ukVUZlxN-f_vVHE_TvA4wQ0lhbroH7m",
      "cabin": "E",
      "chiTag": "",
      "childFareBasis": "",
      "childPrice": 4216.071375385597,
      "childPublishPrice": 4043.4688,
      "childPublishTax": 0,
      "childTax": 1,
      "childTaxType": 0,
      "childTicketPrice": 0,
      "childType": "",
      "childUoTax": 0,
      "childYqTax": 0,
      "childYrTax": 0,
      "ctof": "",
      "currency": "CNY",
      "currencyConversions": [
        {
          "from": "EUR",
          "rate": 7.8974,
          "source": "BOC",
          "timestamp": "2019-08-23T00:37:25Z",
          "to": "CNY"
        },
        {
          "from": "USD",
          "rate": 7,
          "source": "MANUAL",
          "timestamp": "2019-08-14T07:46:00Z",
          "to": "CNY"
        }
      ],
      "data": "99b6660f-ac71-4a10-8745-dcc9b4cf1e76#d29be563-6ec5-48ec-8e39-8f2b45e9a399#MU724_E_MU9829_E_KE1122_E",
      "eligibility": "",
      "evictionMarks": [
        {
          "evictionReason": "Platform[去哪人商旅] 航程内拼接",
          "traceSpans": [
            {
              "application": "night-king",
              "createdAt": null,
              "desc": "PlatformConfig filter",
              "spanId": "",
              "tags": {
                "DisplayNumber": "PFC1907306359",
                "Revision": "5"
              },
              "traceType": "None"
            }
          ]
        }
      ],
      "fareBasis": "",
      "fareCalcLine": "",
      "fareType": "PRIVATE",
      "flightCode": "",
      "infantPrice": 0,
      "infantPublishPrice": 0,
      "infantPublishTax": 0,
      "infantTax": 0,
      "infantTaxType": 0,
      "infantType": "",
      "itinerary": [
        {
          "destinationCity": "SEL",
          "duration": 32700,
          "originCity": "HKG",
          "segment": [
            {
              "accountCode": "",
              "aircraftCode": "321",
              "arrivalAirport": "PVG",
              "arrivalTerminal": "",
              "arrivalTime": "201909231150",
              "arrivalTimeWithOffset": "",
              "availabilitySource": "",
              "baggage": {
                "baggageCheck": false,
                "freeBaggagePiece": -1,
                "freeBaggageWeight": 20
              },
              "bookingClass": "Z",
              "cabin": "E",
              "carrier": "MU",
              "childCabin": "",
              "childFareBasis": "",
              "codeShare": false,
              "connection": false,
              "departureAirport": "HKG",
              "departureTerminal": "",
              "departureTime": "201909230935",
              "departureTimeWithOffset": "",
              "duration": 135,
              "fareBasis": "RSE0WCS2",
              "fareType": "PRIVATE",
              "flightNumber": "MU724",
              "flyTime": 0,
              "key": "",
              "mainSegment": true,
              "marriageGrp": "",
              "operatingCarrier": "MU",
              "operatingFlightNumber": "MU724",
              "seats": 1,
              "status": "",
              "stopCity": [],
              "stopInfo": 0
            },
            {
              "accountCode": "",
              "aircraftCode": "738",
              "arrivalAirport": "PUS",
              "arrivalTerminal": "",
              "arrivalTime": "201909231650",
              "arrivalTimeWithOffset": "",
              "availabilitySource": "",
              "baggage": {
                "baggageCheck": false,
                "freeBaggagePiece": -1,
                "freeBaggageWeight": 20
              },
              "bookingClass": "Z",
              "cabin": "E",
              "carrier": "MU",
              "childCabin": "",
              "childFareBasis": "",
              "codeShare": true,
              "connection": false,
              "departureAirport": "PVG",
              "departureTerminal": "",
              "departureTime": "201909231350",
              "departureTimeWithOffset": "",
              "duration": 120,
              "fareBasis": "RSRWCK",
              "fareType": "PRIVATE",
              "flightNumber": "MU9829",
              "flyTime": 0,
              "key": "",
              "mainSegment": false,
              "marriageGrp": "",
              "operatingCarrier": "FM",
              "operatingFlightNumber": "FM829",
              "seats": 1,
              "status": "",
              "stopCity": [],
              "stopInfo": 0
            },
            {
              "accountCode": "",
              "aircraftCode": "73J",
              "arrivalAirport": "GMP",
              "arrivalTerminal": "",
              "arrivalTime": "201909231940",
              "arrivalTimeWithOffset": "",
              "availabilitySource": "",
              "baggage": {
                "baggageCheck": false,
                "freeBaggagePiece": -1,
                "freeBaggageWeight": 20
              },
              "bookingClass": "N",
              "cabin": "E",
              "carrier": "KE",
              "childCabin": "",
              "childFareBasis": "",
              "codeShare": false,
              "connection": false,
              "departureAirport": "PUS",
              "departureTerminal": "",
              "departureTime": "201909231840",
              "departureTimeWithOffset": "",
              "duration": 60,
              "fareBasis": "Y",
              "fareType": "PRIVATE",
              "flightNumber": "KE1122",
              "flyTime": 0,
              "key": "",
              "mainSegment": false,
              "marriageGrp": "",
              "operatingCarrier": "KE",
              "operatingFlightNumber": "KE1122",
              "seats": 1,
              "status": "",
              "stopCity": [],
              "stopInfo": 0
            }
          ],
          "segmentSplicing": true
        }
      ],
      "itinerarySplicing": false,
      "masterCurrency": "CNY",
      "multiTicket": false,
      "nationalType": 0,
      "nationality": "",
      "onlineCheckIn": true,
      "oriAdultPrice": 512,
      "oriAdultTax": 0,
      "oriChildPrice": 512,
      "oriChildTax": 0,
      "oriInfantPrice": 0,
      "oriInfantTax": 0,
      "policyPriceChanges": [
        {
          "adultChange": {
            "absChange": {
              "amount": 4,
              "currency": "USD"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 0
            },
            "totalChange": {
              "amount": -84,
              "currency": "CNY"
            }
          },
          "childChange": {
            "absChange": {
              "amount": 4,
              "currency": "USD"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 0
            },
            "totalChange": {
              "amount": -84,
              "currency": "CNY"
            }
          },
          "displayNumber": "IC1908021687",
          "infantChange": null,
          "isFeeApplyToProvider": true,
          "otherAbsChangeDetails": [
            {
              "absTotal": {
                "amount": 15,
                "currency": "USD"
              },
              "desc": "INCENTIVE_RECEIVABLE",
              "totalChange": {
                "amount": 105,
                "currency": "CNY"
              }
            }
          ],
          "otherPercentageChangeDetails": [],
          "policyDesc": "IncentivePolicy:IC1908021687",
          "policyId": "5d4411fa73e1340001e3e890",
          "policyType": "INCENTIVE"
        },
        {
          "adultChange": {
            "absChange": {
              "amount": 5,
              "currency": "CNY"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 5.99
            },
            "totalChange": {
              "amount": 257.6025753855973,
              "currency": "CNY"
            }
          },
          "childChange": {
            "absChange": {
              "amount": 5,
              "currency": "CNY"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 5.99
            },
            "totalChange": {
              "amount": 257.6025753855973,
              "currency": "CNY"
            }
          },
          "displayNumber": "PF1907210860",
          "infantChange": {
            "absChange": {
              "amount": 5,
              "currency": "CNY"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 5.99
            },
            "totalChange": {
              "amount": 5.318583129454313,
              "currency": "CNY"
            }
          },
          "isFeeApplyToProvider": true,
          "otherAbsChangeDetails": [],
          "otherPercentageChangeDetails": [],
          "policyDesc": "PlatformPolicy:PF1907210860",
          "policyId": "5d342d9bf24d1c0001195a24",
          "policyType": "PLATFORM"
        }
      ],
      "posLocation": "CN",
      "priceType": 0,
      "providerCurrency": "EUR",
      "providerName": "skypk",
      "providerType": "PROVIDER_API",
      "routingId": "",
      "rule": {
        "changeBeforeDep": 0,
        "changeBeforeDepFee": 0,
        "changeDetail": null,
        "cnRemark": "",
        "currency": "CNY",
        "enRemark": "",
        "manualFareRule": null,
        "miniRule": -404,
        "noShowChange": 0,
        "noShowChangeAfter": 0,
        "noShowChangeAfterFee": 0,
        "noShowChangeFee": 0,
        "noShowRefund": 0,
        "noShowRefundAfter": 0,
        "noShowRefundAfterFee": 0,
        "noShowRefundFee": 0,
        "originRuleFee": {
          "changeAfterFee": -404,
          "changeAfterNoshowFee": -404,
          "changeBeforeFee": -404,
          "changeBeforeNoshowFee": -404,
          "currency": "",
          "refundAfterFee": -404,
          "refundAfterNoshowFee": -404,
          "refundBeforeFee": -404,
          "refundBeforeNoshowFee": -404
        },
        "partEndorse": 0,
        "partEndorsePrice": 0,
        "partRefund": 0,
        "partRefundFee": 0,
        "refundBeforeDep": 0,
        "refundBeforeDepFee": 0,
        "ruleFromOta": -404,
        "useOld": false
      },
      "saleBaggage": false,
      "seats": 1,
      "suitAge": "",
      "ticketInvoiceType": 0,
      "ticketPrice": 0,
      "ticketSource": 0,
      "ticketTimeLimitMinutes": 2880,
      "tof": "",
      "traceSpans": [
        {
          "application": "night-king",
          "createdAt": "2019-08-23T00:51:25.204340466Z",
          "desc": "move amount of 1.000000 from fare price to adult tax",
          "spanId": "c1e2b8f7-7b0a-4f66-a65f-3801cc34e6b8",
          "tags": {},
          "traceType": "None"
        },
        {
          "application": "night-king",
          "createdAt": "2019-08-23T00:51:25.204343943Z",
          "desc": "move amount of 1.000000 from child fare price to child tax",
          "spanId": "e8296cdd-39d1-41ed-965f-b722f55a7dec",
          "tags": {},
          "traceType": "None"
        }
      ],
      "validSegmentsCount": 3,
      "validatingCarrier": "MU",
      "viewPrice": 0
    },
    {
      "accountCode": "",
      "aduTag": "",
      "adultPrice": 4682.686416338687,
      "adultPublishPrice": 4454.1336,
      "adultPublishTax": 0,
      "adultTax": 1,
      "adultTaxType": 0,
      "adultType": "",
      "adultUoTax": 0,
      "adultYqTax": 0,
      "adultYrTax": 0,
      "applyType": 0,
      "arf": "",
      "bookingToken": "ALBG_Q8dS_kKOz7yGrv_oZidlrJbmF4sBHM4AoEiYw7ak7XfWIorOLl94_rLPiMOvJJPdv92ISqDPRU5wOhZf8S59bbPmhvRIFX_4InGlLNmLhyg8CGrNLz5YRoCdgWwqdGU6ih_5g8tjORmwlh-HU_M2R_4JY4JOyN8dAwfJU5UjxegAUJWzkDVqJnuZTVGTIPyVKvEm3Ra4dG1S7qc4XfIJsSHxQARk_Rq8e6YTFqcLTLUyHIJQss-iHxHv01SgEjyHnb8zsroBuyYRiSQBgCZj3rtbfnbuRtupYOobbTJxDdctjjpxfT5ffEpsijPSMl2ibrOPYsp1LZgfibcxzPhHUkUPFxNlg0ob0xmMGV-kZsmF389V38-Pn2uQGauPY27gkouMhon48dghHj9OAVBV1Z-_jdevktQRqqnlHY68DUece5dEBkgJwIwhHMMe-lBLm9NsuFzgt6jftYn-8mM8KzZos5AB-IPMx5pTTpI_yvaH9WER1hTbugTaniLNtqrNvwXeQSpkso1CxAW82Q==",
      "cabin": "E",
      "chiTag": "",
      "childFareBasis": "",
      "childPrice": 4682.686416338687,
      "childPublishPrice": 4454.1336,
      "childPublishTax": 0,
      "childTax": 1,
      "childTaxType": 0,
      "childTicketPrice": 0,
      "childType": "",
      "childUoTax": 0,
      "childYqTax": 0,
      "childYrTax": 0,
      "ctof": "",
      "currency": "CNY",
      "currencyConversions": [
        {
          "from": "EUR",
          "rate": 7.8974,
          "source": "BOC",
          "timestamp": "2019-08-23T00:37:25Z",
          "to": "CNY"
        },
        {
          "from": "USD",
          "rate": 7,
          "source": "MANUAL",
          "timestamp": "2019-08-14T07:46:00Z",
          "to": "CNY"
        }
      ],
      "data": "99b6660f-ac71-4a10-8745-dcc9b4cf1e76#6bedbc40-451e-4709-a21e-8c307bedd02f#KA312_E_BX8826_E",
      "eligibility": "",
      "evictionMarks": [
        {
          "evictionReason": "Platform[去哪人商旅] 航程内拼接",
          "traceSpans": [
            {
              "application": "night-king",
              "createdAt": null,
              "desc": "PlatformConfig filter",
              "spanId": "",
              "tags": {
                "DisplayNumber": "PFC1907306359",
                "Revision": "5"
              },
              "traceType": "None"
            }
          ]
        }
      ],
      "fareBasis": "",
      "fareCalcLine": "",
      "fareType": "PRIVATE",
      "flightCode": "",
      "infantPrice": 0,
      "infantPublishPrice": 0,
      "infantPublishTax": 0,
      "infantTax": 0,
      "infantTaxType": 0,
      "infantType": "",
      "itinerary": [
        {
          "destinationCity": "SEL",
          "duration": 26400,
          "originCity": "HKG",
          "segment": [
            {
              "accountCode": "",
              "aircraftCode": "320",
              "arrivalAirport": "PUS",
              "arrivalTerminal": "",
              "arrivalTime": "201909231705",
              "arrivalTimeWithOffset": "",
              "availabilitySource": "",
              "baggage": {
                "baggageCheck": false,
                "freeBaggagePiece": -1,
                "freeBaggageWeight": 15
              },
              "bookingClass": "N",
              "cabin": "E",
              "carrier": "KA",
              "childCabin": "",
              "childFareBasis": "",
              "codeShare": false,
              "connection": false,
              "departureAirport": "HKG",
              "departureTerminal": "",
              "departureTime": "201909231235",
              "departureTimeWithOffset": "",
              "duration": 210,
              "fareBasis": "SLARRWG8",
              "fareType": "PRIVATE",
              "flightNumber": "KA312",
              "flyTime": 0,
              "key": "",
              "mainSegment": true,
              "marriageGrp": "",
              "operatingCarrier": "KA",
              "operatingFlightNumber": "KA312",
              "seats": 1,
              "status": "",
              "stopCity": [],
              "stopInfo": 0
            },
            {
              "accountCode": "",
              "aircraftCode": "",
              "arrivalAirport": "GMP",
              "arrivalTerminal": "",
              "arrivalTime": "201909232055",
              "arrivalTimeWithOffset": "",
              "availabilitySource": "",
              "baggage": {
                "baggageCheck": true,
                "freeBaggagePiece": -1,
                "freeBaggageWeight": 15
              },
              "bookingClass": "G",
              "cabin": "E",
              "carrier": "BX",
              "childCabin": "",
              "childFareBasis": "",
              "codeShare": false,
              "connection": false,
              "departureAirport": "PUS",
              "departureTerminal": "",
              "departureTime": "201909232000",
              "departureTimeWithOffset": "",
              "duration": 55,
              "fareBasis": "",
              "fareType": "PRIVATE",
              "flightNumber": "BX8826",
              "flyTime": 0,
              "key": "",
              "mainSegment": false,
              "marriageGrp": "",
              "operatingCarrier": "",
              "operatingFlightNumber": "",
              "seats": 1,
              "status": "",
              "stopCity": [],
              "stopInfo": 0
            }
          ],
          "segmentSplicing": true
        }
      ],
      "itinerarySplicing": false,
      "masterCurrency": "CNY",
      "multiTicket": false,
      "nationalType": 0,
      "nationality": "",
      "onlineCheckIn": true,
      "oriAdultPrice": 564,
      "oriAdultTax": 0,
      "oriChildPrice": 564,
      "oriChildTax": 0,
      "oriInfantPrice": 0,
      "oriInfantTax": 0,
      "policyPriceChanges": [
        {
          "adultChange": {
            "absChange": {
              "amount": 4,
              "currency": "USD"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 0
            },
            "totalChange": {
              "amount": -56,
              "currency": "CNY"
            }
          },
          "childChange": {
            "absChange": {
              "amount": 4,
              "currency": "USD"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 0
            },
            "totalChange": {
              "amount": -56,
              "currency": "CNY"
            }
          },
          "displayNumber": "IC1908021687",
          "infantChange": null,
          "isFeeApplyToProvider": true,
          "otherAbsChangeDetails": [
            {
              "absTotal": {
                "amount": 10,
                "currency": "USD"
              },
              "desc": "INCENTIVE_RECEIVABLE",
              "totalChange": {
                "amount": 70,
                "currency": "CNY"
              }
            }
          ],
          "otherPercentageChangeDetails": [],
          "policyDesc": "IncentivePolicy:IC1908021687",
          "policyId": "5d4411fa73e1340001e3e890",
          "policyType": "INCENTIVE"
        },
        {
          "adultChange": {
            "absChange": {
              "amount": 5,
              "currency": "CNY"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 5.99
            },
            "totalChange": {
              "amount": 285.5528163386874,
              "currency": "CNY"
            }
          },
          "childChange": {
            "absChange": {
              "amount": 5,
              "currency": "CNY"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 5.99
            },
            "totalChange": {
              "amount": 285.5528163386874,
              "currency": "CNY"
            }
          },
          "displayNumber": "PF1907210860",
          "infantChange": {
            "absChange": {
              "amount": 5,
              "currency": "CNY"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 5.99
            },
            "totalChange": {
              "amount": 5.318583129454313,
              "currency": "CNY"
            }
          },
          "isFeeApplyToProvider": true,
          "otherAbsChangeDetails": [],
          "otherPercentageChangeDetails": [],
          "policyDesc": "PlatformPolicy:PF1907210860",
          "policyId": "5d342d9bf24d1c0001195a24",
          "policyType": "PLATFORM"
        }
      ],
      "posLocation": "CN",
      "priceType": 0,
      "providerCurrency": "EUR",
      "providerName": "skypk",
      "providerType": "PROVIDER_API",
      "routingId": "",
      "rule": {
        "changeBeforeDep": 0,
        "changeBeforeDepFee": 0,
        "changeDetail": null,
        "cnRemark": "",
        "currency": "CNY",
        "enRemark": "",
        "manualFareRule": null,
        "miniRule": -404,
        "noShowChange": 0,
        "noShowChangeAfter": 0,
        "noShowChangeAfterFee": 0,
        "noShowChangeFee": 0,
        "noShowRefund": 0,
        "noShowRefundAfter": 0,
        "noShowRefundAfterFee": 0,
        "noShowRefundFee": 0,
        "originRuleFee": {
          "changeAfterFee": -404,
          "changeAfterNoshowFee": -404,
          "changeBeforeFee": -404,
          "changeBeforeNoshowFee": -404,
          "currency": "",
          "refundAfterFee": -404,
          "refundAfterNoshowFee": -404,
          "refundBeforeFee": -404,
          "refundBeforeNoshowFee": -404
        },
        "partEndorse": 0,
        "partEndorsePrice": 0,
        "partRefund": 0,
        "partRefundFee": 0,
        "refundBeforeDep": 0,
        "refundBeforeDepFee": 0,
        "ruleFromOta": -404,
        "useOld": false
      },
      "saleBaggage": false,
      "seats": 1,
      "suitAge": "",
      "ticketInvoiceType": 0,
      "ticketPrice": 0,
      "ticketSource": 0,
      "ticketTimeLimitMinutes": 2880,
      "tof": "",
      "traceSpans": [
        {
          "application": "night-king",
          "createdAt": "2019-08-23T00:51:25.204386506Z",
          "desc": "move amount of 1.000000 from fare price to adult tax",
          "spanId": "09ff0292-a365-4835-ab50-8989773a8e3a",
          "tags": {},
          "traceType": "None"
        },
        {
          "application": "night-king",
          "createdAt": "2019-08-23T00:51:25.204389777Z",
          "desc": "move amount of 1.000000 from child fare price to child tax",
          "spanId": "c06b861c-0322-4b13-8a64-5df94e587230",
          "tags": {},
          "traceType": "None"
        }
      ],
      "validSegmentsCount": 2,
      "validatingCarrier": "KA",
      "viewPrice": 0
    },
    {
      "accountCode": "",
      "aduTag": "",
      "adultPrice": 4896.519625571747,
      "adultPublishPrice": 4683.1582,
      "adultPublishTax": 0,
      "adultTax": 1,
      "adultTaxType": 0,
      "adultType": "",
      "adultUoTax": 0,
      "adultYqTax": 0,
      "adultYrTax": 0,
      "applyType": 0,
      "arf": "",
      "bookingToken": "AXhNqE0B2dw6U39dPN731CFx-JbatNPSz3YS6rJnDEhiok8q_JhU1zam3nfx4fEOKW5ZyGXJl-20JmawrxJbwn3Nz5wvNrtmsrZsOBhvBrh5oPrnzJUD2AhGzO1xBW45Jr2eixkmdWbk4Kje6sscPMOU8T0axEGb7fG1PrJvz76DeH-Nv7z02DodJwWh9K16Gr_i8hked8NjSLDc-RYTNKWl0pqkkUwFOsuDYkyaoG4YDmt1ApI2LKuUcSuClVpfZJGjfsWvVv0EGSvB5rQ75-QSEYSKLe-qvzKihu0ZhKTe9QmIGiJUn9Nn4WovnKj60YUnyhis6MCWmlCzpSo5YVj46hRiPkUvvOzPoTRiyLg0qweEG5XgPDA8pzWe5Vj0ZL3MumteTq66Vld_6R4zAmzKtpmgza5o7QBHGeZLgv-AyzvjIO89cN5OP8peAygo8EaGDPXA_2JDsS7VunuWxgP9xk0DgQfBLOR9uEdKQlXjANMmB2AIvVG8RG5WS_B4poUbzIbQaKDRtJHQsv8Q5xbxHK3P64gLXLGktVxTgilo=",
      "cabin": "E",
      "chiTag": "",
      "childFareBasis": "",
      "childPrice": 4896.519625571747,
      "childPublishPrice": 4683.1582,
      "childPublishTax": 0,
      "childTax": 1,
      "childTaxType": 0,
      "childTicketPrice": 0,
      "childType": "",
      "childUoTax": 0,
      "childYqTax": 0,
      "childYrTax": 0,
      "ctof": "",
      "currency": "CNY",
      "currencyConversions": [
        {
          "from": "EUR",
          "rate": 7.8974,
          "source": "BOC",
          "timestamp": "2019-08-23T00:37:25Z",
          "to": "CNY"
        },
        {
          "from": "USD",
          "rate": 7,
          "source": "MANUAL",
          "timestamp": "2019-08-14T07:46:00Z",
          "to": "CNY"
        }
      ],
      "data": "99b6660f-ac71-4a10-8745-dcc9b4cf1e76#dde77d4a-7769-48b6-81a2-ce5c794d1f7f#BR892_E_OZ9744_E_KE1122_E",
      "eligibility": "",
      "evictionMarks": [
        {
          "evictionReason": "Platform[去哪人商旅] 航程内拼接",
          "traceSpans": [
            {
              "application": "night-king",
              "createdAt": null,
              "desc": "PlatformConfig filter",
              "spanId": "",
              "tags": {
                "DisplayNumber": "PFC1907306359",
                "Revision": "5"
              },
              "traceType": "None"
            }
          ]
        }
      ],
      "fareBasis": "",
      "fareCalcLine": "",
      "fareType": "PRIVATE",
      "flightCode": "",
      "infantPrice": 0,
      "infantPublishPrice": 0,
      "infantPublishTax": 0,
      "infantTax": 0,
      "infantTaxType": 0,
      "infantType": "",
      "itinerary": [
        {
          "destinationCity": "SEL",
          "duration": 31800,
          "originCity": "HKG",
          "segment": [
            {
              "accountCode": "",
              "aircraftCode": "789",
              "arrivalAirport": "TPE",
              "arrivalTerminal": "",
              "arrivalTime": "201909231140",
              "arrivalTimeWithOffset": "",
              "availabilitySource": "",
              "baggage": {
                "baggageCheck": false,
                "freeBaggagePiece": -1,
                "freeBaggageWeight": 15
              },
              "bookingClass": "S",
              "cabin": "E",
              "carrier": "BR",
              "childCabin": "",
              "childFareBasis": "",
              "codeShare": false,
              "connection": false,
              "departureAirport": "HKG",
              "departureTerminal": "",
              "departureTime": "201909230950",
              "departureTimeWithOffset": "",
              "duration": 110,
              "fareBasis": "BLOWHK",
              "fareType": "PRIVATE",
              "flightNumber": "BR892",
              "flyTime": 0,
              "key": "",
              "mainSegment": false,
              "marriageGrp": "",
              "operatingCarrier": "BR",
              "operatingFlightNumber": "BR892",
              "seats": 1,
              "status": "",
              "stopCity": [],
              "stopInfo": 0
            },
            {
              "accountCode": "",
              "aircraftCode": "321",
              "arrivalAirport": "PUS",
              "arrivalTerminal": "",
              "arrivalTime": "201909231630",
              "arrivalTimeWithOffset": "",
              "availabilitySource": "",
              "baggage": {
                "baggageCheck": false,
                "freeBaggagePiece": -1,
                "freeBaggageWeight": 15
              },
              "bookingClass": "L",
              "cabin": "E",
              "carrier": "OZ",
              "childCabin": "",
              "childFareBasis": "",
              "codeShare": true,
              "connection": false,
              "departureAirport": "TPE",
              "departureTerminal": "",
              "departureTime": "201909231320",
              "departureTimeWithOffset": "",
              "duration": 130,
              "fareBasis": "ELOSKBX",
              "fareType": "PRIVATE",
              "flightNumber": "OZ9744",
              "flyTime": 0,
              "key": "",
              "mainSegment": true,
              "marriageGrp": "",
              "operatingCarrier": "BX",
              "operatingFlightNumber": "BX794",
              "seats": 1,
              "status": "",
              "stopCity": [],
              "stopInfo": 0
            },
            {
              "accountCode": "",
              "aircraftCode": "73J",
              "arrivalAirport": "GMP",
              "arrivalTerminal": "",
              "arrivalTime": "201909231940",
              "arrivalTimeWithOffset": "",
              "availabilitySource": "",
              "baggage": {
                "baggageCheck": true,
                "freeBaggagePiece": -1,
                "freeBaggageWeight": 15
              },
              "bookingClass": "N",
              "cabin": "E",
              "carrier": "KE",
              "childCabin": "",
              "childFareBasis": "",
              "codeShare": false,
              "connection": false,
              "departureAirport": "PUS",
              "departureTerminal": "",
              "departureTime": "201909231840",
              "departureTimeWithOffset": "",
              "duration": 60,
              "fareBasis": "Y",
              "fareType": "PRIVATE",
              "flightNumber": "KE1122",
              "flyTime": 0,
              "key": "",
              "mainSegment": false,
              "marriageGrp": "",
              "operatingCarrier": "KE",
              "operatingFlightNumber": "KE1122",
              "seats": 1,
              "status": "",
              "stopCity": [],
              "stopInfo": 0
            }
          ],
          "segmentSplicing": true
        }
      ],
      "itinerarySplicing": false,
      "masterCurrency": "CNY",
      "multiTicket": false,
      "nationalType": 0,
      "nationality": "",
      "onlineCheckIn": false,
      "oriAdultPrice": 593,
      "oriAdultTax": 0,
      "oriChildPrice": 593,
      "oriChildTax": 0,
      "oriInfantPrice": 0,
      "oriInfantTax": 0,
      "policyPriceChanges": [
        {
          "adultChange": {
            "absChange": {
              "amount": 4,
              "currency": "USD"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 0
            },
            "totalChange": {
              "amount": -84,
              "currency": "CNY"
            }
          },
          "childChange": {
            "absChange": {
              "amount": 4,
              "currency": "USD"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 0
            },
            "totalChange": {
              "amount": -84,
              "currency": "CNY"
            }
          },
          "displayNumber": "IC1908021687",
          "infantChange": null,
          "isFeeApplyToProvider": true,
          "otherAbsChangeDetails": [
            {
              "absTotal": {
                "amount": 15,
                "currency": "USD"
              },
              "desc": "INCENTIVE_RECEIVABLE",
              "totalChange": {
                "amount": 105,
                "currency": "CNY"
              }
            }
          ],
          "otherPercentageChangeDetails": [],
          "policyDesc": "IncentivePolicy:IC1908021687",
          "policyId": "5d4411fa73e1340001e3e890",
          "policyType": "INCENTIVE"
        },
        {
          "adultChange": {
            "absChange": {
              "amount": 5,
              "currency": "CNY"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 5.99
            },
            "totalChange": {
              "amount": 298.3614255717477,
              "currency": "CNY"
            }
          },
          "childChange": {
            "absChange": {
              "amount": 5,
              "currency": "CNY"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 5.99
            },
            "totalChange": {
              "amount": 298.3614255717477,
              "currency": "CNY"
            }
          },
          "displayNumber": "PF1907210860",
          "infantChange": {
            "absChange": {
              "amount": 5,
              "currency": "CNY"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 5.99
            },
            "totalChange": {
              "amount": 5.318583129454313,
              "currency": "CNY"
            }
          },
          "isFeeApplyToProvider": true,
          "otherAbsChangeDetails": [],
          "otherPercentageChangeDetails": [],
          "policyDesc": "PlatformPolicy:PF1907210860",
          "policyId": "5d342d9bf24d1c0001195a24",
          "policyType": "PLATFORM"
        }
      ],
      "posLocation": "CN",
      "priceType": 0,
      "providerCurrency": "EUR",
      "providerName": "skypk",
      "providerType": "PROVIDER_API",
      "routingId": "",
      "rule": {
        "changeBeforeDep": 0,
        "changeBeforeDepFee": 0,
        "changeDetail": null,
        "cnRemark": "",
        "currency": "CNY",
        "enRemark": "",
        "manualFareRule": null,
        "miniRule": -404,
        "noShowChange": 0,
        "noShowChangeAfter": 0,
        "noShowChangeAfterFee": 0,
        "noShowChangeFee": 0,
        "noShowRefund": 0,
        "noShowRefundAfter": 0,
        "noShowRefundAfterFee": 0,
        "noShowRefundFee": 0,
        "originRuleFee": {
          "changeAfterFee": -404,
          "changeAfterNoshowFee": -404,
          "changeBeforeFee": -404,
          "changeBeforeNoshowFee": -404,
          "currency": "",
          "refundAfterFee": -404,
          "refundAfterNoshowFee": -404,
          "refundBeforeFee": -404,
          "refundBeforeNoshowFee": -404
        },
        "partEndorse": 0,
        "partEndorsePrice": 0,
        "partRefund": 0,
        "partRefundFee": 0,
        "refundBeforeDep": 0,
        "refundBeforeDepFee": 0,
        "ruleFromOta": -404,
        "useOld": false
      },
      "saleBaggage": false,
      "seats": 1,
      "suitAge": "",
      "ticketInvoiceType": 0,
      "ticketPrice": 0,
      "ticketSource": 0,
      "ticketTimeLimitMinutes": 2880,
      "tof": "",
      "traceSpans": [
        {
          "application": "night-king",
          "createdAt": "2019-08-23T00:51:25.204435394Z",
          "desc": "move amount of 1.000000 from fare price to adult tax",
          "spanId": "ff891619-3bd7-4b1e-bbcb-870220e8cfdd",
          "tags": {},
          "traceType": "None"
        },
        {
          "application": "night-king",
          "createdAt": "2019-08-23T00:51:25.204438739Z",
          "desc": "move amount of 1.000000 from child fare price to child tax",
          "spanId": "04a49c7e-769d-4125-a26f-de8a15fda497",
          "tags": {},
          "traceType": "None"
        }
      ],
      "validSegmentsCount": 3,
      "validatingCarrier": "BR",
      "viewPrice": 0
    },
    {
      "accountCode": "",
      "aduTag": "",
      "adultPrice": 5438.740027656632,
      "adultPublishPrice": 5164.8996,
      "adultPublishTax": 0,
      "adultTax": 1,
      "adultTaxType": 0,
      "adultType": "",
      "adultUoTax": 0,
      "adultYqTax": 0,
      "adultYrTax": 0,
      "applyType": 0,
      "arf": "",
      "bookingToken": "ASAy4ZszFa6u9fQfRzqnynr8VByWFlWjVPObvmRNVTAnfn38wgkWPtBoywR3vuTzc-WgGHjm_d2dQObm5lI24Xgnhn3fg_0tfPZnRTXvgGjqFKf_MwaqhhK8iONwVIRGrn3AkM_k07BCteuMhNUzPQDBkjOu3abp6N4jHNoYSEnVuxUbELRdTAiVeXOPFDJGjOzfcfoPLFXONbUdMYBskwLPpr2c68fTyrj5R9i8mcd8XJF_XhBK7qIWMmNtalmjq_NprqjS-0PUmMUz1oU_eaPUNgh-wi6zrXcYTPh4IkV4rTBGng65AJWwZsGXxN52fRFFjHN6qABkct9SQTm7tA-dO5kYxX-gKvJpw1Yj9v0gJfn6pzjXgpRBKrrfo72zwxazguAH8DNqN72EYBjS1J3auc_lZQT_jEzwUYq39xzjGQjzFlhS3C_BO1NoyqPB9NGNZjtu0O5WPk0EUYhBaMsJoH4n_x6aFX0_aWCEZijKH5R7_ReAllQH7p20ROV8Y",
      "cabin": "E",
      "chiTag": "",
      "childFareBasis": "",
      "childPrice": 5438.740027656632,
      "childPublishPrice": 5164.8996,
      "childPublishTax": 0,
      "childTax": 1,
      "childTaxType": 0,
      "childTicketPrice": 0,
      "childType": "",
      "childUoTax": 0,
      "childYqTax": 0,
      "childYrTax": 0,
      "ctof": "",
      "currency": "CNY",
      "currencyConversions": [
        {
          "from": "EUR",
          "rate": 7.8974,
          "source": "BOC",
          "timestamp": "2019-08-23T00:37:25Z",
          "to": "CNY"
        },
        {
          "from": "USD",
          "rate": 7,
          "source": "MANUAL",
          "timestamp": "2019-08-14T07:46:00Z",
          "to": "CNY"
        }
      ],
      "data": "99b6660f-ac71-4a10-8745-dcc9b4cf1e76#88a44806-017a-4aa9-87c6-d31bea255882#KA838_E_FM823_E",
      "eligibility": "",
      "evictionMarks": [
        {
          "evictionReason": "Platform[去哪人商旅] 航程内拼接",
          "traceSpans": [
            {
              "application": "night-king",
              "createdAt": null,
              "desc": "PlatformConfig filter",
              "spanId": "",
              "tags": {
                "DisplayNumber": "PFC1907306359",
                "Revision": "5"
              },
              "traceType": "None"
            }
          ]
        }
      ],
      "fareBasis": "",
      "fareCalcLine": "",
      "fareType": "PRIVATE",
      "flightCode": "",
      "infantPrice": 0,
      "infantPublishPrice": 0,
      "infantPublishTax": 0,
      "infantTax": 0,
      "infantTaxType": 0,
      "infantType": "",
      "itinerary": [
        {
          "destinationCity": "SEL",
          "duration": 29700,
          "originCity": "HKG",
          "segment": [
            {
              "accountCode": "",
              "aircraftCode": "333",
              "arrivalAirport": "SHA",
              "arrivalTerminal": "",
              "arrivalTime": "201909231205",
              "arrivalTimeWithOffset": "",
              "availabilitySource": "",
              "baggage": {
                "baggageCheck": false,
                "freeBaggagePiece": -1,
                "freeBaggageWeight": 20
              },
              "bookingClass": "N",
              "cabin": "E",
              "carrier": "KA",
              "childCabin": "",
              "childFareBasis": "",
              "codeShare": false,
              "connection": false,
              "departureAirport": "HKG",
              "departureTerminal": "",
              "departureTime": "201909230935",
              "departureTimeWithOffset": "",
              "duration": 150,
              "fareBasis": "YOW2",
              "fareType": "PRIVATE",
              "flightNumber": "KA838",
              "flyTime": 0,
              "key": "",
              "mainSegment": true,
              "marriageGrp": "",
              "operatingCarrier": "KA",
              "operatingFlightNumber": "KA838",
              "seats": 1,
              "status": "",
              "stopCity": [],
              "stopInfo": 0
            },
            {
              "accountCode": "",
              "aircraftCode": "333",
              "arrivalAirport": "GMP",
              "arrivalTerminal": "",
              "arrivalTime": "201909231850",
              "arrivalTimeWithOffset": "",
              "availabilitySource": "",
              "baggage": {
                "baggageCheck": true,
                "freeBaggagePiece": -1,
                "freeBaggageWeight": 20
              },
              "bookingClass": "S",
              "cabin": "E",
              "carrier": "FM",
              "childCabin": "",
              "childFareBasis": "",
              "codeShare": false,
              "connection": false,
              "departureAirport": "SHA",
              "departureTerminal": "",
              "departureTime": "201909231605",
              "departureTimeWithOffset": "",
              "duration": 105,
              "fareBasis": "SSRWCK",
              "fareType": "PRIVATE",
              "flightNumber": "FM823",
              "flyTime": 0,
              "key": "",
              "mainSegment": false,
              "marriageGrp": "",
              "operatingCarrier": "FM",
              "operatingFlightNumber": "FM823",
              "seats": 1,
              "status": "",
              "stopCity": [],
              "stopInfo": 0
            }
          ],
          "segmentSplicing": true
        }
      ],
      "itinerarySplicing": false,
      "masterCurrency": "CNY",
      "multiTicket": false,
      "nationalType": 0,
      "nationality": "",
      "onlineCheckIn": true,
      "oriAdultPrice": 654,
      "oriAdultTax": 0,
      "oriChildPrice": 654,
      "oriChildTax": 0,
      "oriInfantPrice": 0,
      "oriInfantTax": 0,
      "policyPriceChanges": [
        {
          "adultChange": {
            "absChange": {
              "amount": 4,
              "currency": "USD"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 0
            },
            "totalChange": {
              "amount": -56,
              "currency": "CNY"
            }
          },
          "childChange": {
            "absChange": {
              "amount": 4,
              "currency": "USD"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 0
            },
            "totalChange": {
              "amount": -56,
              "currency": "CNY"
            }
          },
          "displayNumber": "IC1908021687",
          "infantChange": null,
          "isFeeApplyToProvider": true,
          "otherAbsChangeDetails": [
            {
              "absTotal": {
                "amount": 10,
                "currency": "USD"
              },
              "desc": "INCENTIVE_RECEIVABLE",
              "totalChange": {
                "amount": 70,
                "currency": "CNY"
              }
            }
          ],
          "otherPercentageChangeDetails": [],
          "policyDesc": "IncentivePolicy:IC1908021687",
          "policyId": "5d4411fa73e1340001e3e890",
          "policyType": "INCENTIVE"
        },
        {
          "adultChange": {
            "absChange": {
              "amount": 5,
              "currency": "CNY"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 5.99
            },
            "totalChange": {
              "amount": 330.84042765663224,
              "currency": "CNY"
            }
          },
          "childChange": {
            "absChange": {
              "amount": 5,
              "currency": "CNY"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 5.99
            },
            "totalChange": {
              "amount": 330.84042765663224,
              "currency": "CNY"
            }
          },
          "displayNumber": "PF1907210860",
          "infantChange": {
            "absChange": {
              "amount": 5,
              "currency": "CNY"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 5.99
            },
            "totalChange": {
              "amount": 5.318583129454313,
              "currency": "CNY"
            }
          },
          "isFeeApplyToProvider": true,
          "otherAbsChangeDetails": [],
          "otherPercentageChangeDetails": [],
          "policyDesc": "PlatformPolicy:PF1907210860",
          "policyId": "5d342d9bf24d1c0001195a24",
          "policyType": "PLATFORM"
        }
      ],
      "posLocation": "CN",
      "priceType": 0,
      "providerCurrency": "EUR",
      "providerName": "skypk",
      "providerType": "PROVIDER_API",
      "routingId": "",
      "rule": {
        "changeBeforeDep": 0,
        "changeBeforeDepFee": 0,
        "changeDetail": null,
        "cnRemark": "",
        "currency": "CNY",
        "enRemark": "",
        "manualFareRule": null,
        "miniRule": -404,
        "noShowChange": 0,
        "noShowChangeAfter": 0,
        "noShowChangeAfterFee": 0,
        "noShowChangeFee": 0,
        "noShowRefund": 0,
        "noShowRefundAfter": 0,
        "noShowRefundAfterFee": 0,
        "noShowRefundFee": 0,
        "originRuleFee": {
          "changeAfterFee": -404,
          "changeAfterNoshowFee": -404,
          "changeBeforeFee": -404,
          "changeBeforeNoshowFee": -404,
          "currency": "",
          "refundAfterFee": -404,
          "refundAfterNoshowFee": -404,
          "refundBeforeFee": -404,
          "refundBeforeNoshowFee": -404
        },
        "partEndorse": 0,
        "partEndorsePrice": 0,
        "partRefund": 0,
        "partRefundFee": 0,
        "refundBeforeDep": 0,
        "refundBeforeDepFee": 0,
        "ruleFromOta": -404,
        "useOld": false
      },
      "saleBaggage": false,
      "seats": 1,
      "suitAge": "",
      "ticketInvoiceType": 0,
      "ticketPrice": 0,
      "ticketSource": 0,
      "ticketTimeLimitMinutes": 2880,
      "tof": "",
      "traceSpans": [
        {
          "application": "night-king",
          "createdAt": "2019-08-23T00:51:25.204482740Z",
          "desc": "move amount of 1.000000 from fare price to adult tax",
          "spanId": "3ae56ad7-dc49-4450-b371-559f5e0b3567",
          "tags": {},
          "traceType": "None"
        },
        {
          "application": "night-king",
          "createdAt": "2019-08-23T00:51:25.204485993Z",
          "desc": "move amount of 1.000000 from child fare price to child tax",
          "spanId": "ccd32bba-3642-4ade-a8cb-659f661b08ca",
          "tags": {},
          "traceType": "None"
        }
      ],
      "validSegmentsCount": 2,
      "validatingCarrier": "KA",
      "viewPrice": 0
    },
    {
      "accountCode": "",
      "aduTag": "",
      "adultPrice": 5463.941814700564,
      "adultPublishPrice": 5188.5918,
      "adultPublishTax": 0,
      "adultTax": 1,
      "adultTaxType": 0,
      "adultType": "",
      "adultUoTax": 0,
      "adultYqTax": 0,
      "adultYrTax": 0,
      "applyType": 0,
      "arf": "",
      "bookingToken": "AeEg1UklV0kLLoyMXdEVLehv9JGuvHZz3agYIIcdFYyuJyOTt-DPduQDLjuOH_vR_oDsSXkL5gegm_MGoqdyWU_f9VImBlOBwzRdSJRUEOJFgHpwFVkUxPpxLKcpusQYcmvML49EtNGaMpB_ar4Vj2_0NUufysmTXAn6nketrEHP2riXEm00vEMs-wd-XYS4mSR1sQOzbYu8NTWX6zmc6ufV7-7icBIg9IXiw9uUO9mOsxH40FFGG-8Mp0wfZjCvq2-UtMWgjBO222Gc-RE8fjM3VN3AIKvpZaGQ3nq3-vIa-1lHFXl4L6DBebpt36ays0vxdAoVCkt7tfUwnUqsGTahW22gZvDmfzo2xeMLCRjB7E3rly5mVzs67C6BhpO1iFoKu3B0OqgXwnRAyJ_w-ehEaM6YrFA1hZMASx6f-LzCKrCQU7IpGfiefPlsgAuW4j5xiHuUkvRCgGuz2YPJO1RfqQNEwhFOzs9pHdcc3UfTZPVxu2VjEf0M2RnHFfm2EHHqYqR6GXF5zulsL_yaCIQ==",
      "cabin": "E",
      "chiTag": "",
      "childFareBasis": "",
      "childPrice": 5463.941814700564,
      "childPublishPrice": 5188.5918,
      "childPublishTax": 0,
      "childTax": 1,
      "childTaxType": 0,
      "childTicketPrice": 0,
      "childType": "",
      "childUoTax": 0,
      "childYqTax": 0,
      "childYrTax": 0,
      "ctof": "",
      "currency": "CNY",
      "currencyConversions": [
        {
          "from": "EUR",
          "rate": 7.8974,
          "source": "BOC",
          "timestamp": "2019-08-23T00:37:25Z",
          "to": "CNY"
        },
        {
          "from": "USD",
          "rate": 7,
          "source": "MANUAL",
          "timestamp": "2019-08-14T07:46:00Z",
          "to": "CNY"
        }
      ],
      "data": "99b6660f-ac71-4a10-8745-dcc9b4cf1e76#4ed04098-78d2-4383-90bc-333a82443a70#KA312_E_KE1124_E",
      "eligibility": "",
      "evictionMarks": [
        {
          "evictionReason": "Platform[去哪人商旅] 航程内拼接",
          "traceSpans": [
            {
              "application": "night-king",
              "createdAt": null,
              "desc": "PlatformConfig filter",
              "spanId": "",
              "tags": {
                "DisplayNumber": "PFC1907306359",
                "Revision": "5"
              },
              "traceType": "None"
            }
          ]
        }
      ],
      "fareBasis": "",
      "fareCalcLine": "",
      "fareType": "PRIVATE",
      "flightCode": "",
      "infantPrice": 0,
      "infantPublishPrice": 0,
      "infantPublishTax": 0,
      "infantTax": 0,
      "infantTaxType": 0,
      "infantType": "",
      "itinerary": [
        {
          "destinationCity": "SEL",
          "duration": 25500,
          "originCity": "HKG",
          "segment": [
            {
              "accountCode": "",
              "aircraftCode": "320",
              "arrivalAirport": "PUS",
              "arrivalTerminal": "",
              "arrivalTime": "201909231705",
              "arrivalTimeWithOffset": "",
              "availabilitySource": "",
              "baggage": {
                "baggageCheck": false,
                "freeBaggagePiece": -1,
                "freeBaggageWeight": 20
              },
              "bookingClass": "N",
              "cabin": "E",
              "carrier": "KA",
              "childCabin": "",
              "childFareBasis": "",
              "codeShare": false,
              "connection": false,
              "departureAirport": "HKG",
              "departureTerminal": "",
              "departureTime": "201909231235",
              "departureTimeWithOffset": "",
              "duration": 210,
              "fareBasis": "SLARRWG8",
              "fareType": "PRIVATE",
              "flightNumber": "KA312",
              "flyTime": 0,
              "key": "",
              "mainSegment": true,
              "marriageGrp": "",
              "operatingCarrier": "KA",
              "operatingFlightNumber": "KA312",
              "seats": 1,
              "status": "",
              "stopCity": [],
              "stopInfo": 0
            },
            {
              "accountCode": "",
              "aircraftCode": "739",
              "arrivalAirport": "GMP",
              "arrivalTerminal": "",
              "arrivalTime": "201909232040",
              "arrivalTimeWithOffset": "",
              "availabilitySource": "",
              "baggage": {
                "baggageCheck": true,
                "freeBaggagePiece": -1,
                "freeBaggageWeight": 20
              },
              "bookingClass": "N",
              "cabin": "E",
              "carrier": "KE",
              "childCabin": "",
              "childFareBasis": "",
              "codeShare": false,
              "connection": false,
              "departureAirport": "PUS",
              "departureTerminal": "",
              "departureTime": "201909231940",
              "departureTimeWithOffset": "",
              "duration": 60,
              "fareBasis": "Y",
              "fareType": "PRIVATE",
              "flightNumber": "KE1124",
              "flyTime": 0,
              "key": "",
              "mainSegment": false,
              "marriageGrp": "",
              "operatingCarrier": "KE",
              "operatingFlightNumber": "KE1124",
              "seats": 1,
              "status": "",
              "stopCity": [],
              "stopInfo": 0
            }
          ],
          "segmentSplicing": true
        }
      ],
      "itinerarySplicing": false,
      "masterCurrency": "CNY",
      "multiTicket": false,
      "nationalType": 0,
      "nationality": "",
      "onlineCheckIn": true,
      "oriAdultPrice": 657,
      "oriAdultTax": 0,
      "oriChildPrice": 657,
      "oriChildTax": 0,
      "oriInfantPrice": 0,
      "oriInfantTax": 0,
      "policyPriceChanges": [
        {
          "adultChange": {
            "absChange": {
              "amount": 4,
              "currency": "USD"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 0
            },
            "totalChange": {
              "amount": -56,
              "currency": "CNY"
            }
          },
          "childChange": {
            "absChange": {
              "amount": 4,
              "currency": "USD"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 0
            },
            "totalChange": {
              "amount": -56,
              "currency": "CNY"
            }
          },
          "displayNumber": "IC1908021687",
          "infantChange": null,
          "isFeeApplyToProvider": true,
          "otherAbsChangeDetails": [
            {
              "absTotal": {
                "amount": 10,
                "currency": "USD"
              },
              "desc": "INCENTIVE_RECEIVABLE",
              "totalChange": {
                "amount": 70,
                "currency": "CNY"
              }
            }
          ],
          "otherPercentageChangeDetails": [],
          "policyDesc": "IncentivePolicy:IC1908021687",
          "policyId": "5d4411fa73e1340001e3e890",
          "policyType": "INCENTIVE"
        },
        {
          "adultChange": {
            "absChange": {
              "amount": 5,
              "currency": "CNY"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 5.99
            },
            "totalChange": {
              "amount": 332.3500147005638,
              "currency": "CNY"
            }
          },
          "childChange": {
            "absChange": {
              "amount": 5,
              "currency": "CNY"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 5.99
            },
            "totalChange": {
              "amount": 332.3500147005638,
              "currency": "CNY"
            }
          },
          "displayNumber": "PF1907210860",
          "infantChange": {
            "absChange": {
              "amount": 5,
              "currency": "CNY"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 5.99
            },
            "totalChange": {
              "amount": 5.318583129454313,
              "currency": "CNY"
            }
          },
          "isFeeApplyToProvider": true,
          "otherAbsChangeDetails": [],
          "otherPercentageChangeDetails": [],
          "policyDesc": "PlatformPolicy:PF1907210860",
          "policyId": "5d342d9bf24d1c0001195a24",
          "policyType": "PLATFORM"
        }
      ],
      "posLocation": "CN",
      "priceType": 0,
      "providerCurrency": "EUR",
      "providerName": "skypk",
      "providerType": "PROVIDER_API",
      "routingId": "",
      "rule": {
        "changeBeforeDep": 0,
        "changeBeforeDepFee": 0,
        "changeDetail": null,
        "cnRemark": "",
        "currency": "CNY",
        "enRemark": "",
        "manualFareRule": null,
        "miniRule": -404,
        "noShowChange": 0,
        "noShowChangeAfter": 0,
        "noShowChangeAfterFee": 0,
        "noShowChangeFee": 0,
        "noShowRefund": 0,
        "noShowRefundAfter": 0,
        "noShowRefundAfterFee": 0,
        "noShowRefundFee": 0,
        "originRuleFee": {
          "changeAfterFee": -404,
          "changeAfterNoshowFee": -404,
          "changeBeforeFee": -404,
          "changeBeforeNoshowFee": -404,
          "currency": "",
          "refundAfterFee": -404,
          "refundAfterNoshowFee": -404,
          "refundBeforeFee": -404,
          "refundBeforeNoshowFee": -404
        },
        "partEndorse": 0,
        "partEndorsePrice": 0,
        "partRefund": 0,
        "partRefundFee": 0,
        "refundBeforeDep": 0,
        "refundBeforeDepFee": 0,
        "ruleFromOta": -404,
        "useOld": false
      },
      "saleBaggage": false,
      "seats": 1,
      "suitAge": "",
      "ticketInvoiceType": 0,
      "ticketPrice": 0,
      "ticketSource": 0,
      "ticketTimeLimitMinutes": 2880,
      "tof": "",
      "traceSpans": [
        {
          "application": "night-king",
          "createdAt": "2019-08-23T00:51:25.204528724Z",
          "desc": "move amount of 1.000000 from fare price to adult tax",
          "spanId": "c90e09a5-f21a-4067-8dd6-6db42447038b",
          "tags": {},
          "traceType": "None"
        },
        {
          "application": "night-king",
          "createdAt": "2019-08-23T00:51:25.204531859Z",
          "desc": "move amount of 1.000000 from child fare price to child tax",
          "spanId": "767bcea2-476c-4e17-9a2a-15d77a1084d8",
          "tags": {},
          "traceType": "None"
        }
      ],
      "validSegmentsCount": 2,
      "validatingCarrier": "KA",
      "viewPrice": 0
    },
    {
      "accountCode": "",
      "aduTag": "",
      "adultPrice": 5644.172641208383,
      "adultPublishPrice": 5386.026800000001,
      "adultPublishTax": 0,
      "adultTax": 1,
      "adultTaxType": 0,
      "adultType": "",
      "adultUoTax": 0,
      "adultYqTax": 0,
      "adultYrTax": 0,
      "applyType": 0,
      "arf": "",
      "bookingToken": "AQyw3EnA5WaRq2iCGBssaacN_LtikEjfjkKxZeheO5pTAoot2CxLzKyVz1EFB8ECABMy04bbqEf_kdGpCXLrB5CGdkIZ8lp8i01-k5sOzGWe2aZH5fL_JQ0aCysRKHzrIuRtSEeFhjXYBO2dk3ap5bP3FzV6ZSAbfWRjKABJNHMb7LSdP3hCjHdlBp09J9r-c3MZnzQVdJ99EM1Z4IqSr-jIuHZrdcgevDxj_Dqy08V6gQW7g_d7uv_3JJaFRKnyQ_UaLiHZ4byPdXm9bvrK_d4rzWA8Zhie6fPU_zkGuybrid1hrMsW4ldIiEVOPBD-BkQo0zSFzgrT7l_PWBEgI0Ex4BfLmJUSH83BqFDQ90yAn2d7mewbJ1Niw7JYOJhkaUKyrjQM4qNG8zLqEM0oN1dif_SesuvRT2RTYrZXLZ0cl0AhiplnSsBm9YLoXC-ck3LjwDr2cHwUTXCFpivVrnyJ-EmRkAv2gOuWLgEZmlagsP5cLJV348lRcKuZcb3RL",
      "cabin": "E",
      "chiTag": "",
      "childFareBasis": "",
      "childPrice": 5644.172641208383,
      "childPublishPrice": 5386.026800000001,
      "childPublishTax": 0,
      "childTax": 1,
      "childTaxType": 0,
      "childTicketPrice": 0,
      "childType": "",
      "childUoTax": 0,
      "childYqTax": 0,
      "childYrTax": 0,
      "ctof": "",
      "currency": "CNY",
      "currencyConversions": [
        {
          "from": "EUR",
          "rate": 7.8974,
          "source": "BOC",
          "timestamp": "2019-08-23T00:37:25Z",
          "to": "CNY"
        },
        {
          "from": "USD",
          "rate": 7,
          "source": "MANUAL",
          "timestamp": "2019-08-14T07:46:00Z",
          "to": "CNY"
        }
      ],
      "data": "99b6660f-ac71-4a10-8745-dcc9b4cf1e76#a8f87e91-5b48-4fec-a2e5-40eeb0482f1b#CI922_E_CI9698_E_BX8820_E",
      "eligibility": "",
      "evictionMarks": [
        {
          "evictionReason": "Platform[去哪人商旅] 航程内拼接",
          "traceSpans": [
            {
              "application": "night-king",
              "createdAt": null,
              "desc": "PlatformConfig filter",
              "spanId": "",
              "tags": {
                "DisplayNumber": "PFC1907306359",
                "Revision": "5"
              },
              "traceType": "None"
            }
          ]
        }
      ],
      "fareBasis": "",
      "fareCalcLine": "",
      "fareType": "PRIVATE",
      "flightCode": "",
      "infantPrice": 0,
      "infantPublishPrice": 0,
      "infantPublishTax": 0,
      "infantTax": 0,
      "infantTaxType": 0,
      "infantType": "",
      "itinerary": [
        {
          "destinationCity": "SEL",
          "duration": 31500,
          "originCity": "HKG",
          "segment": [
            {
              "accountCode": "",
              "aircraftCode": "333",
              "arrivalAirport": "TPE",
              "arrivalTerminal": "",
              "arrivalTime": "201909231000",
              "arrivalTimeWithOffset": "",
              "availabilitySource": "",
              "baggage": {
                "baggageCheck": false,
                "freeBaggagePiece": -1,
                "freeBaggageWeight": 15
              },
              "bookingClass": "S",
              "cabin": "E",
              "carrier": "CI",
              "childCabin": "",
              "childFareBasis": "",
              "codeShare": false,
              "connection": false,
              "departureAirport": "HKG",
              "departureTerminal": "",
              "departureTime": "201909230810",
              "departureTimeWithOffset": "",
              "duration": 110,
              "fareBasis": "YHOHK",
              "fareType": "PRIVATE",
              "flightNumber": "CI922",
              "flyTime": 0,
              "key": "",
              "mainSegment": false,
              "marriageGrp": "",
              "operatingCarrier": "CI",
              "operatingFlightNumber": "CI922",
              "seats": 1,
              "status": "",
              "stopCity": [],
              "stopInfo": 0
            },
            {
              "accountCode": "",
              "aircraftCode": "Non",
              "arrivalAirport": "PUS",
              "arrivalTerminal": "",
              "arrivalTime": "201909231500",
              "arrivalTimeWithOffset": "",
              "availabilitySource": "",
              "baggage": {
                "baggageCheck": false,
                "freeBaggagePiece": -1,
                "freeBaggageWeight": 15
              },
              "bookingClass": "S",
              "cabin": "E",
              "carrier": "CI",
              "childCabin": "",
              "childFareBasis": "",
              "codeShare": true,
              "connection": false,
              "departureAirport": "TPE",
              "departureTerminal": "",
              "departureTime": "201909231135",
              "departureTimeWithOffset": "",
              "duration": 145,
              "fareBasis": "YHOHK",
              "fareType": "PRIVATE",
              "flightNumber": "CI9698",
              "flyTime": 0,
              "key": "",
              "mainSegment": true,
              "marriageGrp": "",
              "operatingCarrier": "KE",
              "operatingFlightNumber": "KE698",
              "seats": 1,
              "status": "",
              "stopCity": [],
              "stopInfo": 0
            },
            {
              "accountCode": "",
              "aircraftCode": "",
              "arrivalAirport": "GMP",
              "arrivalTerminal": "",
              "arrivalTime": "201909231755",
              "arrivalTimeWithOffset": "",
              "availabilitySource": "",
              "baggage": {
                "baggageCheck": true,
                "freeBaggagePiece": -1,
                "freeBaggageWeight": 15
              },
              "bookingClass": "G",
              "cabin": "E",
              "carrier": "BX",
              "childCabin": "",
              "childFareBasis": "",
              "codeShare": false,
              "connection": false,
              "departureAirport": "PUS",
              "departureTerminal": "",
              "departureTime": "201909231700",
              "departureTimeWithOffset": "",
              "duration": 55,
              "fareBasis": "",
              "fareType": "PRIVATE",
              "flightNumber": "BX8820",
              "flyTime": 0,
              "key": "",
              "mainSegment": false,
              "marriageGrp": "",
              "operatingCarrier": "",
              "operatingFlightNumber": "",
              "seats": 1,
              "status": "",
              "stopCity": [],
              "stopInfo": 0
            }
          ],
          "segmentSplicing": true
        }
      ],
      "itinerarySplicing": false,
      "masterCurrency": "CNY",
      "multiTicket": false,
      "nationalType": 0,
      "nationality": "",
      "onlineCheckIn": true,
      "oriAdultPrice": 682,
      "oriAdultTax": 0,
      "oriChildPrice": 682,
      "oriChildTax": 0,
      "oriInfantPrice": 0,
      "oriInfantTax": 0,
      "policyPriceChanges": [
        {
          "adultChange": {
            "absChange": {
              "amount": 4,
              "currency": "USD"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 0
            },
            "totalChange": {
              "amount": -84,
              "currency": "CNY"
            }
          },
          "childChange": {
            "absChange": {
              "amount": 4,
              "currency": "USD"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 0
            },
            "totalChange": {
              "amount": -84,
              "currency": "CNY"
            }
          },
          "displayNumber": "IC1908021687",
          "infantChange": null,
          "isFeeApplyToProvider": true,
          "otherAbsChangeDetails": [
            {
              "absTotal": {
                "amount": 15,
                "currency": "USD"
              },
              "desc": "INCENTIVE_RECEIVABLE",
              "totalChange": {
                "amount": 105,
                "currency": "CNY"
              }
            }
          ],
          "otherPercentageChangeDetails": [],
          "policyDesc": "IncentivePolicy:IC1908021687",
          "policyId": "5d4411fa73e1340001e3e890",
          "policyType": "INCENTIVE"
        },
        {
          "adultChange": {
            "absChange": {
              "amount": 5,
              "currency": "CNY"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 5.99
            },
            "totalChange": {
              "amount": 343.1458412083821,
              "currency": "CNY"
            }
          },
          "childChange": {
            "absChange": {
              "amount": 5,
              "currency": "CNY"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 5.99
            },
            "totalChange": {
              "amount": 343.1458412083821,
              "currency": "CNY"
            }
          },
          "displayNumber": "PF1907210860",
          "infantChange": {
            "absChange": {
              "amount": 5,
              "currency": "CNY"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 5.99
            },
            "totalChange": {
              "amount": 5.318583129454313,
              "currency": "CNY"
            }
          },
          "isFeeApplyToProvider": true,
          "otherAbsChangeDetails": [],
          "otherPercentageChangeDetails": [],
          "policyDesc": "PlatformPolicy:PF1907210860",
          "policyId": "5d342d9bf24d1c0001195a24",
          "policyType": "PLATFORM"
        }
      ],
      "posLocation": "CN",
      "priceType": 0,
      "providerCurrency": "EUR",
      "providerName": "skypk",
      "providerType": "PROVIDER_API",
      "routingId": "",
      "rule": {
        "changeBeforeDep": 0,
        "changeBeforeDepFee": 0,
        "changeDetail": null,
        "cnRemark": "",
        "currency": "CNY",
        "enRemark": "",
        "manualFareRule": null,
        "miniRule": -404,
        "noShowChange": 0,
        "noShowChangeAfter": 0,
        "noShowChangeAfterFee": 0,
        "noShowChangeFee": 0,
        "noShowRefund": 0,
        "noShowRefundAfter": 0,
        "noShowRefundAfterFee": 0,
        "noShowRefundFee": 0,
        "originRuleFee": {
          "changeAfterFee": -404,
          "changeAfterNoshowFee": -404,
          "changeBeforeFee": -404,
          "changeBeforeNoshowFee": -404,
          "currency": "",
          "refundAfterFee": -404,
          "refundAfterNoshowFee": -404,
          "refundBeforeFee": -404,
          "refundBeforeNoshowFee": -404
        },
        "partEndorse": 0,
        "partEndorsePrice": 0,
        "partRefund": 0,
        "partRefundFee": 0,
        "refundBeforeDep": 0,
        "refundBeforeDepFee": 0,
        "ruleFromOta": -404,
        "useOld": false
      },
      "saleBaggage": false,
      "seats": 1,
      "suitAge": "",
      "ticketInvoiceType": 0,
      "ticketPrice": 0,
      "ticketSource": 0,
      "ticketTimeLimitMinutes": 2880,
      "tof": "",
      "traceSpans": [
        {
          "application": "night-king",
          "createdAt": "2019-08-23T00:51:25.204573488Z",
          "desc": "move amount of 1.000000 from fare price to adult tax",
          "spanId": "5e76bd36-e5a8-4a3d-9b39-48157b709784",
          "tags": {},
          "traceType": "None"
        },
        {
          "application": "night-king",
          "createdAt": "2019-08-23T00:51:25.204576686Z",
          "desc": "move amount of 1.000000 from child fare price to child tax",
          "spanId": "3dfaef8b-ea0a-4354-ae37-22f0f4dc3d19",
          "tags": {},
          "traceType": "None"
        }
      ],
      "validSegmentsCount": 3,
      "validatingCarrier": "CI",
      "viewPrice": 0
    },
    {
      "accountCode": "",
      "aduTag": "",
      "adultPrice": 7732.102648654399,
      "adultPublishPrice": 7320.8898,
      "adultPublishTax": 0,
      "adultTax": 1,
      "adultTaxType": 0,
      "adultType": "",
      "adultUoTax": 0,
      "adultYqTax": 0,
      "adultYrTax": 0,
      "applyType": 0,
      "arf": "",
      "bookingToken": "ADAZGask9U6IRSL7IKeDC-Ub7Z2DF6dUf_WC02eiyCnnbXiFj-d7NWOZbW3v0HOJs1rbUkGRA8T_yRVm3tS3d2IDuPMne5E7bdnxkX7WFV6MckBG6_bSd7MpeNLl9pwjrxQvIjfK57M2I5zdfF2d0IpagRt1blz19nJ2QIM83SPEKiQ7V59MPpBe6sDdFmnu_N6O_x7HuTIEq10rVcnbKm-pFlCzLpBWs0kApFFMe9seftJpUcsfym_31KzblEqYKtbxU2NTF72HkgLYvum8cfJPLIcQ2FfBDrik5h9CbKpcOvonppUjnCCYJCvarYiOiTDo9uJmpoEdPEECepA-KVm0nCMBX2K7aJf1j8cPaXSW5KX1_d9RwQJYP51gPOWfWb78sBv0QZ3e1zuFRz1kAuB8fF3CYS5HmEQBG_LDwoSiwJ0cyXMviEdzD7_rgC7qE09jJiNje2LWOrwFqFfGWOiDBDNlIeavU4tuoJeTwUZtaF1SZG7YPv-CtxmY24RJK1jP5eiDETbSriFoSwb7Rvw==",
      "cabin": "E",
      "chiTag": "",
      "childFareBasis": "",
      "childPrice": 7732.102648654399,
      "childPublishPrice": 7320.8898,
      "childPublishTax": 0,
      "childTax": 1,
      "childTaxType": 0,
      "childTicketPrice": 0,
      "childType": "",
      "childUoTax": 0,
      "childYqTax": 0,
      "childYrTax": 0,
      "ctof": "",
      "currency": "CNY",
      "currencyConversions": [
        {
          "from": "EUR",
          "rate": 7.8974,
          "source": "BOC",
          "timestamp": "2019-08-23T00:37:25Z",
          "to": "CNY"
        },
        {
          "from": "USD",
          "rate": 7,
          "source": "MANUAL",
          "timestamp": "2019-08-14T07:46:00Z",
          "to": "CNY"
        }
      ],
      "data": "99b6660f-ac71-4a10-8745-dcc9b4cf1e76#9cbbcb9e-543e-43bf-a638-96b8ba612e44#CX566_E_OZ115_E",
      "eligibility": "",
      "evictionMarks": [
        {
          "evictionReason": "Platform[去哪人商旅] 航程内拼接",
          "traceSpans": [
            {
              "application": "night-king",
              "createdAt": null,
              "desc": "PlatformConfig filter",
              "spanId": "",
              "tags": {
                "DisplayNumber": "PFC1907306359",
                "Revision": "5"
              },
              "traceType": "None"
            }
          ]
        }
      ],
      "fareBasis": "",
      "fareCalcLine": "",
      "fareType": "PRIVATE",
      "flightCode": "",
      "infantPrice": 0,
      "infantPublishPrice": 0,
      "infantPublishTax": 0,
      "infantTax": 0,
      "infantTaxType": 0,
      "infantType": "",
      "itinerary": [
        {
          "destinationCity": "SEL",
          "duration": 29400,
          "originCity": "HKG",
          "segment": [
            {
              "accountCode": "",
              "aircraftCode": "333",
              "arrivalAirport": "KIX",
              "arrivalTerminal": "",
              "arrivalTime": "201909230630",
              "arrivalTimeWithOffset": "",
              "availabilitySource": "",
              "baggage": {
                "baggageCheck": false,
                "freeBaggagePiece": -1,
                "freeBaggageWeight": 20
              },
              "bookingClass": "Q",
              "cabin": "E",
              "carrier": "CX",
              "childCabin": "",
              "childFareBasis": "",
              "codeShare": false,
              "connection": false,
              "departureAirport": "HKG",
              "departureTerminal": "",
              "departureTime": "201909230150",
              "departureTimeWithOffset": "",
              "duration": 220,
              "fareBasis": "NLARRWF8",
              "fareType": "PRIVATE",
              "flightNumber": "CX566",
              "flyTime": 0,
              "key": "",
              "mainSegment": true,
              "marriageGrp": "",
              "operatingCarrier": "CX",
              "operatingFlightNumber": "CX566",
              "seats": 1,
              "status": "",
              "stopCity": [],
              "stopInfo": 0
            },
            {
              "accountCode": "",
              "aircraftCode": "321",
              "arrivalAirport": "ICN",
              "arrivalTerminal": "",
              "arrivalTime": "201909231100",
              "arrivalTimeWithOffset": "",
              "availabilitySource": "",
              "baggage": {
                "baggageCheck": true,
                "freeBaggagePiece": -1,
                "freeBaggageWeight": 20
              },
              "bookingClass": "L",
              "cabin": "E",
              "carrier": "OZ",
              "childCabin": "",
              "childFareBasis": "",
              "codeShare": false,
              "connection": false,
              "departureAirport": "KIX",
              "departureTerminal": "",
              "departureTime": "201909230910",
              "departureTimeWithOffset": "",
              "duration": 110,
              "fareBasis": "QJXOJK",
              "fareType": "PRIVATE",
              "flightNumber": "OZ115",
              "flyTime": 0,
              "key": "",
              "mainSegment": false,
              "marriageGrp": "",
              "operatingCarrier": "OZ",
              "operatingFlightNumber": "OZ115",
              "seats": 1,
              "status": "",
              "stopCity": [],
              "stopInfo": 0
            }
          ],
          "segmentSplicing": true
        }
      ],
      "itinerarySplicing": false,
      "masterCurrency": "CNY",
      "multiTicket": false,
      "nationalType": 0,
      "nationality": "",
      "onlineCheckIn": true,
      "oriAdultPrice": 927,
      "oriAdultTax": 0,
      "oriChildPrice": 927,
      "oriChildTax": 0,
      "oriInfantPrice": 0,
      "oriInfantTax": 0,
      "policyPriceChanges": [
        {
          "adultChange": {
            "absChange": {
              "amount": 4,
              "currency": "USD"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 0
            },
            "totalChange": {
              "amount": -56,
              "currency": "CNY"
            }
          },
          "childChange": {
            "absChange": {
              "amount": 4,
              "currency": "USD"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 0
            },
            "totalChange": {
              "amount": -56,
              "currency": "CNY"
            }
          },
          "displayNumber": "IC1908021687",
          "infantChange": null,
          "isFeeApplyToProvider": true,
          "otherAbsChangeDetails": [
            {
              "absTotal": {
                "amount": 10,
                "currency": "USD"
              },
              "desc": "INCENTIVE_RECEIVABLE",
              "totalChange": {
                "amount": 70,
                "currency": "CNY"
              }
            }
          ],
          "otherPercentageChangeDetails": [],
          "policyDesc": "IncentivePolicy:IC1908021687",
          "policyId": "5d4411fa73e1340001e3e890",
          "policyType": "INCENTIVE"
        },
        {
          "adultChange": {
            "absChange": {
              "amount": 5,
              "currency": "CNY"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 5.99
            },
            "totalChange": {
              "amount": 468.21284865439844,
              "currency": "CNY"
            }
          },
          "childChange": {
            "absChange": {
              "amount": 5,
              "currency": "CNY"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 5.99
            },
            "totalChange": {
              "amount": 468.21284865439844,
              "currency": "CNY"
            }
          },
          "displayNumber": "PF1907210860",
          "infantChange": {
            "absChange": {
              "amount": 5,
              "currency": "CNY"
            },
            "percentageChange": {
              "excludeTax": false,
              "percentage": 5.99
            },
            "totalChange": {
              "amount": 5.318583129454313,
              "currency": "CNY"
            }
          },
          "isFeeApplyToProvider": true,
          "otherAbsChangeDetails": [],
          "otherPercentageChangeDetails": [],
          "policyDesc": "PlatformPolicy:PF1907210860",
          "policyId": "5d342d9bf24d1c0001195a24",
          "policyType": "PLATFORM"
        }
      ],
      "posLocation": "CN",
      "priceType": 0,
      "providerCurrency": "EUR",
      "providerName": "skypk",
      "providerType": "PROVIDER_API",
      "routingId": "",
      "rule": {
        "changeBeforeDep": 0,
        "changeBeforeDepFee": 0,
        "changeDetail": null,
        "cnRemark": "",
        "currency": "CNY",
        "enRemark": "",
        "manualFareRule": null,
        "miniRule": -404,
        "noShowChange": 0,
        "noShowChangeAfter": 0,
        "noShowChangeAfterFee": 0,
        "noShowChangeFee": 0,
        "noShowRefund": 0,
        "noShowRefundAfter": 0,
        "noShowRefundAfterFee": 0,
        "noShowRefundFee": 0,
        "originRuleFee": {
          "changeAfterFee": -404,
          "changeAfterNoshowFee": -404,
          "changeBeforeFee": -404,
          "changeBeforeNoshowFee": -404,
          "currency": "",
          "refundAfterFee": -404,
          "refundAfterNoshowFee": -404,
          "refundBeforeFee": -404,
          "refundBeforeNoshowFee": -404
        },
        "partEndorse": 0,
        "partEndorsePrice": 0,
        "partRefund": 0,
        "partRefundFee": 0,
        "refundBeforeDep": 0,
        "refundBeforeDepFee": 0,
        "ruleFromOta": -404,
        "useOld": false
      },
      "saleBaggage": false,
      "seats": 1,
      "suitAge": "",
      "ticketInvoiceType": 0,
      "ticketPrice": 0,
      "ticketSource": 0,
      "ticketTimeLimitMinutes": 2880,
      "tof": "",
      "traceSpans": [
        {
          "application": "night-king",
          "createdAt": "2019-08-23T00:51:25.203959189Z",
          "desc": "move amount of 1.000000 from fare price to adult tax",
          "spanId": "b2dc2b4a-3f49-4fa9-85f1-e4423af800e9",
          "tags": {},
          "traceType": "None"
        },
        {
          "application": "night-king",
          "createdAt": "2019-08-23T00:51:25.203962424Z",
          "desc": "move amount of 1.000000 from child fare price to child tax",
          "spanId": "57b0aab3-c83e-4d55-8598-a255cf7d9a24",
          "tags": {},
          "traceType": "None"
        }
      ],
      "validSegmentsCount": 2,
      "validatingCarrier": "CX",
      "viewPrice": 0
    }
  ],
  "traceSpans": [
    {
      "application": "night-king",
      "createdAt": "2019-08-23T00:51:20.276498095Z",
      "desc": "night-king search",
      "spanId": "1eccfe70-e763-491d-a24a-782af3628559",
      "tags": {
        "cost": "4928ms"
      },
      "traceType": "None"
    },
    {
      "application": "night-king",
      "createdAt": "2019-08-23T00:51:20.276555494Z",
      "desc": "target providers by w/b rules",
      "spanId": "666f99a6-188f-4662-a2ad-09d86eb2814f",
      "tags": {
        "nk-wb-all-online-providers": "skypk",
        "nk-wb-amsav": "ID: 5d2832ca9bfc9100017edc24, displayNumber: WB1907121683, revision: 9.. Black/White: ALLOW, Online: false",
        "nk-wb-avia": "ID: 5d2832ca9bfc9100017edc24, displayNumber: WB1907121683, revision: 9.. Black/White: ALLOW, Online: false",
        "nk-wb-final-target-providers": "skypk",
        "nk-wb-list": "ID: 5d2832ca9bfc9100017edc24, displayNumber: WB1907121683, revision: 9.",
        "nk-wb-mondee": "ID: 5d2832ca9bfc9100017edc24, displayNumber: WB1907121683, revision: 9.. Black/White: ALLOW, Online: false",
        "nk-wb-myslcc": "ID: 5d2832ca9bfc9100017edc24, displayNumber: WB1907121683, revision: 9.. Black/White: ALLOW, Online: false",
        "nk-wb-mystifly": "ID: 5d2832ca9bfc9100017edc24, displayNumber: WB1907121683, revision: 9.. Black/White: ALLOW, Online: false",
        "nk-wb-sihai": "ID: 5d2832ca9bfc9100017edc24, displayNumber: WB1907121683, revision: 9.. Black/White: ALLOW, Online: false",
        "nk-wb-skypk": "ID: 5d2832ca9bfc9100017edc24, displayNumber: WB1907121683, revision: 9.. Black/White: ALLOW, Online: true",
        "nk-wb-ssanda": "ID: 5d2832ca9bfc9100017edc24, displayNumber: WB1907121683, revision: 9.. Black/White: ALLOW, Online: false",
        "nk-wb-ssatkt": "ID: 5d2832ca9bfc9100017edc24, displayNumber: WB1907121683, revision: 9.. Black/White: ALLOW, Online: false",
        "nk-wb-sscts": "ID: 5d2832ca9bfc9100017edc24, displayNumber: WB1907121683, revision: 9.. Black/White: ALLOW, Online: false",
        "nk-wb-ssgmt": "ID: 5d2832ca9bfc9100017edc24, displayNumber: WB1907121683, revision: 9.. Black/White: ALLOW, Online: false",
        "nk-wb-ssjdu": "ID: 5d2832ca9bfc9100017edc24, displayNumber: WB1907121683, revision: 9.. Black/White: ALLOW, Online: false",
        "nk-wb-sslion": "ID: 5d2832ca9bfc9100017edc24, displayNumber: WB1907121683, revision: 9.. Black/White: ALLOW, Online: false",
        "nk-wb-ttnet": "ID: 5d2832ca9bfc9100017edc24, displayNumber: WB1907121683, revision: 9.. Black/White: ALLOW, Online: false",
        "nk-wb-via": "ID: 5d2832ca9bfc9100017edc24, displayNumber: WB1907121683, revision: 9.. Black/White: ALLOW, Online: false"
      },
      "traceType": "WB"
    },
    {
      "application": "no-one",
      "createdAt": "2019-08-23T00:51:20.276657744Z",
      "desc": "w/b rules",
      "spanId": "3959ff33-da53-479d-86a0-fd3f12904e70",
      "tags": {
        "no-wb": "No Black WB Matched"
      },
      "traceType": "WB"
    },
    {
      "application": "night-king",
      "createdAt": "2019-08-23T00:51:20.279322948Z",
      "desc": "provider search stats",
      "spanId": "08f20101-3b90-4949-a975-d519ac0f6080",
      "tags": {
        "cacheHit": "false",
        "provider": "skypk",
        "searchCost": "4917ms",
        "searchThrottled": "false"
      },
      "traceType": "None"
    }
  ],
  "traceTimers": {
    "self": {
      "application": "night-king",
      "bypassed": false,
      "nickName": "",
      "operation": "search",
      "startAt": "2019-08-23T00:51:20.276509565Z",
      "stopAt": "2019-08-23T00:51:25.205190628Z",
      "timeout": false
    },
    "subTimers": [
      {
        "self": {
          "application": "provider-skypicker",
          "bypassed": false,
          "nickName": "",
          "operation": "search",
          "startAt": "2019-08-23T00:51:20.283367781Z",
          "stopAt": "2019-08-23T00:51:25.189196293Z",
          "timeout": false
        },
        "subTimers": [],
        "traceId": ""
      }
    ],
    "traceId": ""
  }
}
'''

ccc = json.loads(ss)
print(ccc["baseResponse"]["nima"])
print(type(ccc["baseResponse"]["nima"]))

teststr = ''

if teststr or teststr=='':
    print('kongzhi fu')
else:
    print('nothigs')