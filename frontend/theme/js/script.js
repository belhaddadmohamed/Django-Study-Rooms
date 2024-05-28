// // Actions:

// const closeButton = `<svg version="1.1" xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 32 32">
// <title>remove</title>
// <path d="M27.314 6.019l-1.333-1.333-9.98 9.981-9.981-9.981-1.333 1.333 9.981 9.981-9.981 9.98 1.333 1.333 9.981-9.98 9.98 9.98 1.333-1.333-9.98-9.98 9.98-9.981z"></path>
// </svg>
// `;
// const menuButton = `<svg version="1.1" xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 32 32">
// <title>ellipsis-horizontal</title>
// <path d="M16 7.843c-2.156 0-3.908-1.753-3.908-3.908s1.753-3.908 3.908-3.908c2.156 0 3.908 1.753 3.908 3.908s-1.753 3.908-3.908 3.908zM16 1.98c-1.077 0-1.954 0.877-1.954 1.954s0.877 1.954 1.954 1.954c1.077 0 1.954-0.877 1.954-1.954s-0.877-1.954-1.954-1.954z"></path>
// <path d="M16 19.908c-2.156 0-3.908-1.753-3.908-3.908s1.753-3.908 3.908-3.908c2.156 0 3.908 1.753 3.908 3.908s-1.753 3.908-3.908 3.908zM16 14.046c-1.077 0-1.954 0.877-1.954 1.954s0.877 1.954 1.954 1.954c1.077 0 1.954-0.877 1.954-1.954s-0.877-1.954-1.954-1.954z"></path>
// <path d="M16 31.974c-2.156 0-3.908-1.753-3.908-3.908s1.753-3.908 3.908-3.908c2.156 0 3.908 1.753 3.908 3.908s-1.753 3.908-3.908 3.908zM16 26.111c-1.077 0-1.954 0.877-1.954 1.954s0.877 1.954 1.954 1.954c1.077 0 1.954-0.877 1.954-1.954s-0.877-1.954-1.954-1.954z"></path>
// </svg>
// `;

// const actionButtons = document.querySelectorAll('.action-button');

// if (actionButtons) {
//   actionButtons.forEach(button => {
//     button.addEventListener('click', () => {
//       const buttonId = button.dataset.id;
//       let popup = document.querySelector(`.popup-${buttonId}`);
//       console.log(popup);
//       if (popup) {
//         button.innerHTML = menuButton;
//         return popup.remove();
//       }

//       const deleteUrl = button.dataset.deleteUrl;
//       const editUrl = button.dataset.editUrl;
//       button.innerHTML = closeButton;

//       popup = document.createElement('div');
//       popup.classList.add('popup');
//       popup.classList.add(`popup-${buttonId}`);
//       popup.innerHTML = `<a href="${editUrl}">Edit</a>
//       <form action="${deleteUrl}" method="delete">
//         <button type="submit">Delete</button>
//       </form>`;
//       button.insertAdjacentElement('afterend', popup);
//     });
//   });
// }

// Menu

const dropdownMenu = document.querySelector(".dropdown-menu");
const dropdownButton = document.querySelector(".dropdown-button");

if (dropdownButton) {
  dropdownButton.addEventListener("click", () => {
    dropdownMenu.classList.toggle("show");
  });
}

// Upload Image
const photoInput = document.querySelector("#avatar");
const photoPreview = document.querySelector("#preview-avatar");
if (photoInput)
  photoInput.onchange = () => {
    const [file] = photoInput.files;
    if (file) {
      photoPreview.src = URL.createObjectURL(file);
    }
  };

// Scroll to Bottom
const conversationThread = document.querySelector(".room__box");
if (conversationThread) conversationThread.scrollTop = conversationThread.scrollHeight;





// ==============================================
     // index.html
// ==============================================

var roomsTag = document.getElementById('rooms')

buildRooms()
function buildRooms(){  
  var api = 'http://127.0.0.1:8000/api/rooms/'
  fetch(api)
  .then(resp => resp.json())
  .then(function(data){
  var rooms = data
    console.log(rooms)

    for(var i in rooms){
      roomsTag.innerHTML += `
                              <div class="roomListRoom">
                                <div class="roomListRoom__header">
                                  <a href="profile.html" class="roomListRoom__author">
                                    <div class="avatar avatar--small">
                                      <img src="http://127.0.0.1:8000/${rooms[i].host.avatar}" />
                                    </div>
                                    <span>@${rooms[i].host.username}</span>
                                  </a>
                                  <div class="roomListRoom__actions">
                                    <span>${parseInt(rooms[i].days_since_created)} days ago </span>
                                  </div>
                                </div>
                                <div class="roomListRoom__content">
                                  <a href="room.html">${rooms[i].name}</a>
                                  <p>
                                    ${rooms[i].description}
                                  </p>
                                </div>
                                <div class="roomListRoom__meta">
                                  <a href="room.html" class="roomListRoom__joined">
                                    <svg version="1.1" xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 32 32">
                                      <title>user-group</title>
                                      <path
                                        d="M30.539 20.766c-2.69-1.547-5.75-2.427-8.92-2.662 0.649 0.291 1.303 0.575 1.918 0.928 0.715 0.412 1.288 1.005 1.71 1.694 1.507 0.419 2.956 1.003 4.298 1.774 0.281 0.162 0.456 0.487 0.456 0.85v4.65h-4v2h5c0.553 0 1-0.447 1-1v-5.65c0-1.077-0.56-2.067-1.461-2.584z"
                                      ></path>
                                      <path
                                        d="M22.539 20.766c-6.295-3.619-14.783-3.619-21.078 0-0.901 0.519-1.461 1.508-1.461 2.584v5.65c0 0.553 0.447 1 1 1h22c0.553 0 1-0.447 1-1v-5.651c0-1.075-0.56-2.064-1.461-2.583zM22 28h-20v-4.65c0-0.362 0.175-0.688 0.457-0.85 5.691-3.271 13.394-3.271 19.086 0 0.282 0.162 0.457 0.487 0.457 0.849v4.651z"
                                      ></path>
                                      <path
                                        d="M19.502 4.047c0.166-0.017 0.33-0.047 0.498-0.047 2.757 0 5 2.243 5 5s-2.243 5-5 5c-0.168 0-0.332-0.030-0.498-0.047-0.424 0.641-0.944 1.204-1.513 1.716 0.651 0.201 1.323 0.331 2.011 0.331 3.859 0 7-3.141 7-7s-3.141-7-7-7c-0.688 0-1.36 0.131-2.011 0.331 0.57 0.512 1.089 1.075 1.513 1.716z"
                                      ></path>
                                      <path
                                        d="M12 16c3.859 0 7-3.141 7-7s-3.141-7-7-7c-3.859 0-7 3.141-7 7s3.141 7 7 7zM12 4c2.757 0 5 2.243 5 5s-2.243 5-5 5-5-2.243-5-5c0-2.757 2.243-5 5-5z"
                                      ></path>
                                    </svg>
                                    ${rooms[i].participants.length} Joined
                                  </a>
                                  <p class="roomListRoom__topic">${rooms[i].topic.name}</p>
                                </div>
                              </div>
                            `
    }
  })
}



activitiesTag = document.getElementById('activities')

buildActivities()
function buildActivities(){
  var api = 'http://127.0.0.1:8000/api/messages/'
  fetch(api)
  .then(resp => resp.json())
  .then(function(data){
    var messages = data
    for(var message in messages){
      activitiesTag.innerHTML += `
          
                      <div class="activities__box">
                      <div class="activities__boxHeader roomListRoom__header">
                        <a href="profile.html" class="roomListRoom__author">
                          <div class="avatar avatar--small">
                            <img src="http://127.0.0.1:8000/${messages[message].user.avatar}" />
                          </div>
                          <p>
                            @${messages[message].user.username}
                            <span>5 days ago</span>
                          </p>
                        </a>
                        <div class="roomListRoom__actions">
                          <a href="#">
                            <svg version="1.1" xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 32 32">
                              <title>remove</title>
                              <path
                                d="M27.314 6.019l-1.333-1.333-9.98 9.981-9.981-9.981-1.333 1.333 9.981 9.981-9.981 9.98 1.333 1.333 9.981-9.98 9.98 9.98 1.333-1.333-9.98-9.98 9.98-9.981z"
                              ></path>
                            </svg>
                          </a>
                        </div>
                      </div>

                      <div class="activities__boxContent">
                        <p>replied to post “<a href="room.html">${messages[message].room.name}</a>”</p>
                        <div class="activities__boxRoomContent">
                          ${messages[message].body.slice(0,100)}
                        </div>
                      </div>
                    </div>
    
      `
    }
  })

}





var topicsTag = document.getElementById("topics__list") 

buildTopics()
function buildTopics(){

  var api = "http://127.0.0.1:8000/api/topics/"

  fetch(api)
  .then(resp => resp.json())
  .then(function(data){
    var topics = data

    for(var topic in topics){
      topicsTag.innerHTML += `
      <li>
        <a href="/" class="active">${topics[topic].name} <span>${topics[topic].rooms.length}</span></a>
      </li>
      `
    }

  })
}








