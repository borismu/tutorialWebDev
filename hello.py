def app(environ, start_response):

      start_response("200 OK", [
          ("Content-Type", "text/plain"),
      ])
      qs = environ['QUERY_STRING']
      data='\n'.join(st.split('&'))
      return [ data ]