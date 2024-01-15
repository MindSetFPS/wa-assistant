async function askAI(context, prompt){
    var answer = fetch('http://localhost:7861/prompt', {
        method: 'POST',
        body: JSON.stringify({
            max_tokens: 128,
            context: context,
            prompt: prompt
        }),
        headers: {
            'Content-type': 'application/json; charset=UTF-8',
          }
    })
    .then(response => response.json())
    .then(data => answer = data.answer)
    .catch(error => {
        //handle error
    });
    console.log(answer)
    return answer
}

export default askAI; 