
import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';
import LoginPage from './components/LoginPage'
import Note from './components/Note'
import Comment from './components/Comment'
import Notfound from './components/NotFound'
import { Route, Link, BrowserRouter as Router, Switch } from 'react-router-dom'
import Timeline from './components/Timeline';
import MenuList from './components/MenuList'

const routing = (

  < Router>
    <div>
      {/* <ul>
        <li>
          <Link to="/">Home</Link>
        </li>
        <li>
          <Link to="/login">Login</Link>
        </li>
        <li>
          <Link to="/note">Note</Link>
        </li>
        <li>
          <Link to="/comment">Comment</Link>
        </li>
        <li>
          <Link to="/timeline">Timeline</Link>
        </li>
        <li>
          <Link to="/menulist">Menu list</Link>;
        </li>
      </ul> */}
      <Switch>
        <Route exact path="/" component={App} />
        <Route path="/timeline" component={Timeline} />
        <Route path="/login" component={LoginPage} />
        <Route path="/note/:id" component={Note} />
        <Route path="/comment" component={Comment} />
        <Route path="/menulist" component={MenuList} />
        <Route component={Notfound} />
      </Switch>
    </div>
  </Router >
)

ReactDOM.render(routing, document.getElementById('root'));

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
// serviceWorker.unregister();
