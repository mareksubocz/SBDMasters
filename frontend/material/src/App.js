import React from "react";
import Cookies from 'universal-cookie';

import GroupList from "./components/GroupList";
import MenuList from "./components/MenuList";
import Timeline from "./components/Timeline";
import TopAppBar from "./components/TopAppBar";

import {api_test, api_request} from "./api";

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
    xhr.send(JSON.stringify({auth_token : cookies.get('auth_token')}))
  }

  getName() {}

	render() {
	api_request(api_test, 'user/debug', {'omg': 1234})
    this.checkIfLoggedIn()
    return (
      <div>
        <TopAppBar />
        <div style={{
      display: 'flex', /* establish flex container */
          flexDirection: 'row', flexWrap: 'nowrap',
          justifyContent: 'space-between', alignContent: 'center',
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
