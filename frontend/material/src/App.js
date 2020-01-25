import React from "react";
import Timeline from "./components/Timeline";
import MenuList from "./components/MenuList";
import GroupList from "./components/GroupList";
import TopAppBar from "./components/TopAppBar"

class App extends React.Component {
  render() {
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
