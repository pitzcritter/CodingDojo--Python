<form action='/amadon/buy' method='post'>
  {% csrf_token %}
  <select name='quantity'>
     <option>1</option>
     <option>2</option>
     <option>3</option>
  </select>
  <input type='hidden' name='price' value='19.99' />
  <input type='submit' value='Buy!' />
</form>