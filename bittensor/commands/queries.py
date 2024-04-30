API_URL = "https://api.taomarketcap.com/graphql"

TOTAL_NETWORKS_QUERY = """
query TotalNetworks {
  totalNetworks(limit: 1) {
    value
  }
}
"""


FETCH_METAGRAPH_QUERY = """
query FetchSubnets($netUid: [Int!]!) {
  subnets(netUid: $netUid) {
    uids {
      stake(limit: 1) {
        data {
          value
        }
        uid
      }
      rank(limit: 1) {
        uid
        data {
          value
        }
      }
      trust(limit: 1) {
        data {
          value
        }
        uid
      }
      consensus(limit: 1) {
        uid
        data {
          value
        }
      }
      incentive(limit: 1) {
        data {
          value
        }
        uid
      }
      dividends(limit: 1) {
        uid
        data {
          value
        }
      }
      emission(limit: 1) {
        data {
          value
        }
        uid
      }
      validatorTrust(limit: 1) {
        data {
          value
        }
        uid
      }
      axons(limit: 1) {
        data {
          value
        }
        uid
      }
      active(limit: 1) {
        data {
          value
        }
        uid
      }
      lastUpdate(limit: 1) {
        data {
          value
        }
        uid
      }
      coldkey(limit: 1) {
        data {
          value
        }
        uid
      }
      validatorPermit {
        data {
          value
        }
        uid
      }
      hotkey {
        key
        uid
      }
    }
    difficulty(limit: 1) {
      value
    }
  }
  totalIssuance(limit: 1) {
    value
    blockNumber
  }
}
"""

FETCH_HYPERPARAMETERS_QUERY = """
query FetchHyperparameters($netUid: [Int!]!) {
  subnets(netUid: $netUid) {
    rho(limit: 1) {
      value
    }
    kappa(limit: 1) {
      value
    }
    immunityPeriod(limit: 1) {
      value
    }
    maxWeightsLimit(limit: 1) {
      value
    }
    tempo(limit: 1) {
      value
    }
    maxDifficulty(limit: 1) {
      value
    }
    minDifficulty(limit: 1) {
      value
    }
    weightsVersionKey(limit: 1) {
      value
    }
    weightsSetRateLimit(limit: 1) {
      value
    }
    targetRegistrationsPerInterval(limit: 1) {
      value
    }
    activityCutoff(limit: 1) {
      value
    }
    networkRegistrationAllowed(limit: 1) {
      value
    }
    maxBurn(limit: 1) {
      value
    }
    minBurn(limit: 1) {
      value
    }
    bondsMovingAverage(limit: 1) {
      value
    }
    maxRegistrationsPerBlock(limit: 1) {
      value
    }
    servingRateLimit(limit: 1) {
      value
    }
    difficulty(limit: 1) {
      value
    }
    minAllowedWeights(limit: 1) {
      value
    }
    adjustmentAlpha(limit: 1) {
      value
    }
    adjustmentInterval(limit: 1) {
      value
    }
    maxAllowedValidators(limit: 1) {
      value
    }
  }
}
"""
