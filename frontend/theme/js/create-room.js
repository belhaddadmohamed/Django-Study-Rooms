
// ==============================================
     // create-room.html
// ==============================================

// FUNCTION COPIED FROM DJANGO DOCUMENTATTION (CREATE A TOKEN FOR THE FORM) (https://docs.djangoproject.com/fr/4.2/howto/csrf/)
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');



// Create topic options
topic_options = document.getElementById('room_topic_options')

buildTopics()
function buildTopics(){
    var api = 'http://127.0.0.1:8000/api/topics/'
    fetch(api)
    .then(resp => resp.json())
    .then(function(data){
      var topics = data
      for(var i in topics){
          console.log(topics[i].name)
  
          topic_options.innerHTML += `
                  <option value="${topics[i].name}"> ${topics[i].name} </option> `    
      }
    })  
}



// Submit informations to the Api
form_room = document.getElementById('form_room')
room_name = document.getElementById('room_name')
room_topic = document.getElementById('room_topic')
room_about = document.getElementById('room_about')


form_room.addEventListener('submit', (event) => {
    event.preventDefault()
    console.log(room_name.value)
    console.log(room_topic.value)
    console.log(room_about.value)

    var api = 'http://127.0.0.1:8000/api/create-room/'
    fetch(api, {
        method : 'POST',
        headers : {
            'Content-type' : 'application/json',
            'X-CSRFToken' : csrftoken },
        body : JSON.stringify({"host": {"id": 5},
                                "name": room_name.value,
                                "topic": {"name": room_topic.value},
                                "description": room_about.value,
                                "participants": [3]})
    })
    .then(function(response){
        form_room.reset()
    })

    

  
})


