import apache_beam as beam


beam_otions = PipelineOptions(
    runner='',
    project='',
    job_name='',
    temp_location=''
)

pipeline = beam.Pipeline(options=beam_options)



