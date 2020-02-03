import React from "react";
import Timeline from "./components/Timeline";
import MenuList from "./components/MenuList";
import GroupList from "./components/GroupList";
import TopAppBar from "./components/TopAppBar";
import Cookies from 'universal-cookie';

class App extends React.Component {

  checkIfLoggedIn() {
    const cookies = new Cookies();
    var xhr = new XMLHttpRequest()
    xhr.addEventListener('load', () => {
      var response = JSON.parse(xhr.responseText)
      if (response.result === "declined") {
        alert('Nie zalogowany')
        window.location.replace("/login");
      }
    })
    xhr.open('POST', 'http://192.168.2.207:8000/user/check')
    xhr.send(JSON.stringify({ auth_token: cookies.get('auth_token') }))
  }

  getName() {

  }

  render() {
    this.checkIfLoggedIn()
    return (
      <div>
        <TopAppBar />
        <div style={{
          display: 'flex',           /* establish flex container */
          flexDirection: 'row',
          flexWrap: 'nowrap',
          justifyContent: 'space-between',
          alignContent: 'center',
        }}>
          <MenuList></MenuList>
          <Timeline></Timeline>
          <GroupList></GroupList>
        </div >
      </div>
    )
  }
}

export default App
