# Regex
Assistance for those looking to get started using Regular Expressions

## Getting started with understanding Regex.

Regex or Regular Expressions is a very powerful and simple way of searching through text. When I first started coding competitively I was always blown away at how my 10+ line function solution was reduced to 1 line of code! 👀

So lets get started with mastering Regex!

### Example 1 - Email Validation

A common use case of regex is for email validation. Lets take a look: 

Let's break a valid email into 3 parts. For this lets use an example email - david@gmail.com and to keep this simple let's assume that we are validating an email for English speakers. 

1 - The beginning portion of the email is david. This can be any lowercase letter, any capital case letter, or any number. We can represent this in regex by `a-z` `A-Z` and `0-9` respectively. This however will only work if we wanted to return one character. So for example d@gmail.com. This is less than ideal so we express that we want any range of the specified characters by enclosing them in square brackts []. So "[a-zA-Z0-9]" works nicely. 

2 - The portion of the email is the @gmail (no period). To signify that we only want one `@` symbol we use the `+` operator. So our regex pattern so far looks like "[a-zA-Z0-9]+@"

3 - The last portion is .com, finishing our email. Since the `.` is an regex expression we need to use `\` to be able to search for this character. `\.`  . Lastly we want to capture the popular suffixes for an email.. .com, .edu, .dev etc.. To do this we enclose our options inside of parenthesis () which is a capture block in regex. Now that we have that in place we can insert our options using the `|` to signify `or`. So (com|edu|dev) will make our regex expression accept one of the three email suffixes. 

To bring it all together our final regex expression looks like `[a-zA-Z0-9]+@\.(com|edu|dev)`. Nice! ⭐️

Here is a nice [succint video](https://www.youtube.com/watch?v=UQQsYXa1EHs&list=PLKvIeC_eqQbU0ymnKF0QWHwGkSv80ob7Y&index=1) on using regex

More examples to come.. 


