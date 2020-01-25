import React from 'react';
import Note from './Note'

class Timeline extends React.Component {
  state = {
    numNotes: 3
  }

  render() {
    const notes = [];

    for (var i = 0; i < this.state.numNotes; i += 1) {
      notes.push(<Note />);
    };

    return (
      <div style={{ direction: "vertical" }}>
        {notes}
      </div>
    );
  }

  // onAddChild = () => {
  //   this.setState({
  //     numNotes: this.state.numChildren + 1
  //   });
  // }
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
