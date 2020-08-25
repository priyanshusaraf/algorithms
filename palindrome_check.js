var arr = []

var reversed_word = "";
var word = prompt("enter a palindrome word")

for(var i = 0; i <= word.length(); i++){
	arr.push(word[i]);
}
for(var i = 0; i <= word.length(); i++){
	reversed_word += arr.pop()
}
if(reversed_word === word){
	console.log(`${word} is a palindrome`)
}
else{
	console.log(`${word} is not a palindrome`)
}