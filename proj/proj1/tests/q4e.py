test = {
  'name': 'q4e',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> all(bus_cluster_sample.isin(bus['business_id']))
          True
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
