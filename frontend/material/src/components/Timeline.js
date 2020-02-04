import React from 'react';
import Note from './Note'
import NewPostArea from './NewPostArea'
import { Button } from '@material-ui/core';
import { api_request } from '../api'


class Timeline extends React.Component {
  constructor(props) {
    super(props)
    this.addChild = this.addChild.bind(this);
    this.newPostRequest = this.newPostRequest.bind(this);
    this.handleNewPostRequest = this.handleNewPostRequest.bind(this);
    this.newMessageEdited = this.newMessageEdited.bind(this);
  }
  state = {
    newMessage: "",
    notes: []
  }

  newMessageEdited = (childData) => {
    this.setState({ newMessage: childData })
  }

  handleNewPostRequest(response) {
    alert(response)
  }

  newPostRequest() {
    this.addChild()
    // api_request(this.handleNewPostRequest, 'note/create', { 'content': this.state.newMessage })
  }

  addChild() {
    this.state.notes.push("cos")
    this.setState({ state: this.state });
  }

  render() {

    // for (var i = 0; i < this.state.numNotes; i += 1) {
    //   this.state.notes.push(<Note />);
    // };
    // this.state.notes.push(<Note />)
    return (
      <div style={{ direction: "vertical" }}>
        <NewPostArea fullWidth onChange={this.newMessageEdited}></NewPostArea>
        <Button variant="contained" color="primary" fullWidth onClick={this.newPostRequest}>
          Potwierdź</Button>
        {this.state.notes.map(function (item) {
          return <Note content={item} />;
        })}
        {/* {this.state.notes} */}
      </div>
    );
  }
}

export default Timeline
// const ParentComponent = props => (
//   <div className="card calculator">
//     <p><a href="#" onClick={props.addChild}>Add Another Child Component</a></p>
//     <div id="posts-pane">
//       {props.posts}
//     </div>
//   </div>
// );

// const ChildComponent = props => <div>{"I am child " + props.number}</div>;
