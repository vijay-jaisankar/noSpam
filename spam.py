import turicreate
data = turicreate.SFrame.read_csv(
    'SMSSpamCollection',
    header=False,
    delimiter='\t',
    quote_char='\0')
data = data.rename(
    {
        'X1': 'label',
         'X2': 'text'
    })
model = turicreate.text_classifier.create(
    data,
    'label',
    features=['text'],
    max_iterations=100000)
model.save('TextMessageClassifier.model')





