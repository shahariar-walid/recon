import re
from urllib.parse import urlparse, parse_qs, urlencode

def replace_all_param_values(url, new_value="1"):
  parsed_url = urlparse(url)
  query_params = parse_qs(parsed_url.query)

  # Replace all parameter values with the new value
  for param_name in query_params:
    query_params[param_name] = [new_value]

  new_query = urlencode(query_params, doseq=True)
  modified_url = parsed_url._replace(query=new_query).geturl()
  return modified_url


# Replace 'your_file.txt' with the actual file name
with open('urls.txt', 'r') as f:
    file_content = f.read()

#print(file_content)
lines = file_content.splitlines()
url_vector = []
url_vector_pattern = []
url_vector.append(lines[0])
url_vector_pattern.append(replace_all_param_values(lines[0]));
#print(url_vector)
#print(url_vector_pattern)

for line in lines:
  temp = replace_all_param_values(line)
  if temp not in url_vector_pattern:
    url_vector.append(line)
    url_vector_pattern.append(temp)

with open('unique_urls.txt', 'w') as f: 
    for url in url_vector:
        f.write(url + '\n') 


