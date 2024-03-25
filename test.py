html = '''<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>Appwrite Functions Test</title>
  </head>
  <body>
    <h1>Worked 🥳</h1>
  </body>
</html>
'''

def main(context):
    if context.req.method == 'GET':
        return context.res.send(html, 200, {'content-type': 'text/html'})
    return context.res.send('Not found', 404)
