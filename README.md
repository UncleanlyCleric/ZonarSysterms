Repo for employment application homework.

The goal here, was to create a custom API that lists the unique languages for a region.  The list is generated by consuming
the API located at https://restcountries.eu.

On eof the first issues I noted, was that the key 'name' was used multiple times throughout the resultant json.  I 
specifically had to target 'languages' and then 'name' under that.  I did this by iterations, and the assigning tags to 
variables.  I'm certain there's a prettier way to do this, but I will be candid and say that I'm not sure how. 

The next phase populated a list, with each unique language in the region.  Once there, a dictionary was created with the region
as the key, and the languages as the values.  My thinking was it would make for an easier display on a final website.

After that, I created a handler that would show valid regions if someone were to enter invalid data.  Then I created a custom
json 404, since that is what would be expected on query.  Testing was done to ensure the data was correct, and Flask was 
delivering it properly via status codes.

application 

--Flask run

----region injected

------consume api and parse data

----return data or error
