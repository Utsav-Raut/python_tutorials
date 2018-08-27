from bs4 import BeautifulSoup

html_doc = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>My WebPpage</title>
</head>
<body>
  <div id="section-1">
  <h3 data-hello="hi">Hello</h3>
  <img src="https://source.unsplash.com/200x200/?nature,water" />
  <p>Eiusmod enim magna labore fugiat culpa eiusmod
  officia cupidatat occaecat duis sit exercitation.</p>
  </div>
  <div id="section-2">
    <ul class="items">
        <li class="item"><a href="#">Item 1</a></li>
        <li class="item"><a href="#">Item 2</a></li>
        <li class="item"><a href="#">Item 3</a></li>
        <li class="item"><a href="#">Item 4</a></li>
        <li class="item"><a href="#">Item 5</a></li>
    </ul>
    </div>
</body>
</html>
"""
soup = BeautifulSoup(html_doc, 'html.parser')

#Direct
print(soup.body)
