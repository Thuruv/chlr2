def rainfall_pivot_chart_view(request):
    ds = DataPool( \
           series=
            [{'options': {
                'source': Report.objects.all()},
              'terms': [
                'process',
                'worker',
                'count',
                ]}
             ])

    cht = Chart(
            datasource = ds,
            series_options =
              [{'options':{
                  'type': 'column',
                  'stacking': True},
                'terms':{
                  'worker': [
                    'process',
                    'count']
                  }}],
            chart_options =
              {'title': {
                   'text': 'Weather Data of Boston and Houston'},
               'xAxis': {
                    'title': {
                       'text': 'Month number'}}})
        #Step 3: Send the PivotChart object to the template.
    return render_to_response('chart.html', {'weatherchart': cht})
