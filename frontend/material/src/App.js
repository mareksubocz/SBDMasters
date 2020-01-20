import React from "react";
import Note from "./components/Note"
import Comment from "./components/Comment"

class App extends React.Component {
  render() {
    return (
      <div>
        <Note></Note>
        <Comment></Comment>
      </div>
    )
  }
}

export default App
