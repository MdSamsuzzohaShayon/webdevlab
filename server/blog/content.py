import html

def encode_html(html_str):
    encoded_str = html.escape(html_str)
    return encoded_str

# Example HTML string
sample_html = '<div>This is <b>bold</b> text.</div>'

# Encode HTML entities
encoded_html = encode_html(sample_html)

# Print the result
print(encoded_html)


import html

def decode_html(encoded_html):
    decoded_str = html.unescape(encoded_html)
    return decoded_str

# Example encoded HTML string
encoded_sample_html = '&lt;div&gt;This is &lt;b&gt;bold&lt;/b&gt; text.&lt;/div&gt;'

# Decode HTML entities
decoded_html = decode_html(encoded_sample_html)

# Print the result
print(decoded_html)