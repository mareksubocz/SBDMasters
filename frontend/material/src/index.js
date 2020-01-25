
import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';
import LoginPage from './components/LoginPage'
import RegisterPage from './components/RegisterPage'
import Note from './components/Note'
import Comment from './components/Comment'
import Notfound from './components/NotFound'
import { Route, BrowserRouter as Router, Switch } from 'react-router-dom'
import Timeline from './components/Timeline';
import MenuList from './components/MenuList'

const routing = (

  < Router>
    <div>
      <Switch>
        <Route exact path="/" component={App} />
        <Route path="/timeline" component={Timeline} />
        <Route path="/login" component={LoginPage} />
        <Route path="/register" component={RegisterPage} />
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
