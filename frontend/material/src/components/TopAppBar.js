import React, { useState } from "react";
import PropTypes from "prop-types";
import { withStyles } from "@material-ui/core/styles";
import AppBar from "@material-ui/core/AppBar";
import Toolbar from "@material-ui/core/Toolbar";
import Typography from "@material-ui/core/Typography";
import IconButton from "@material-ui/core/IconButton";
import MenuIcon from "@material-ui/icons/Menu";
import MenuItem from "@material-ui/core/MenuItem";
import Select from "@material-ui/core/Select";
import LogoutIcon from "@material-ui/icons/ExitToApp"
import Cookies from 'universal-cookie';
import Button from '@material-ui/core/Button'

const styles = {
  root: {
    flexGrow: 1,
  },
  grow: {
    flexGrow: 1,
  },
  menuButton: {
    marginLeft: -12,
    marginRight: 20
  },
  selectRoot: {
    color: "white",
    marginRight: 400,
    variant: "filled",
    minWidth: 200,
  }
};


function ButtonAppBar(props) {
  const [age, setAge] = useState(10);
  const { classes } = props;

  function logoutUser() {
    const cookies = new Cookies();
    cookies.remove('auth_token');
    window.location.replace("/login");
  }

  const handleChange = event => {
    setAge(event.target.value);
  };
  return (
    <div className={classes.root}>
      <AppBar position="static">
        <Toolbar>
          <IconButton
            className={classes.menuButton}
            color="inherit"
            aria-label="Menu"
          >
            <MenuIcon />
          </IconButton>
          <Typography variant="h6" color="inherit" className={classes.grow}>
            {props.name}
          </Typography>
          <Select
            value={age}
            onChange={handleChange}
            inputProps={{
              name: "age",
              id: "age-simple"
            }}
            className={classes.selectRoot}
          >
            <MenuItem value="">
              <em>None</em>
            </MenuItem>
            <MenuItem value={10}>Ten</MenuItem>
            <MenuItem value={20}>Twenty</MenuItem>
            <MenuItem value={30}>Thirty</MenuItem>
          </Select>
          <Button onClick={logoutUser}>
            <LogoutIcon style={{ color: "white" }}></LogoutIcon>
          </Button>
        </Toolbar>
      </AppBar>
    </div>
  );
}

ButtonAppBar.propTypes = {
  classes: PropTypes.object.isRequired
};

export default withStyles(styles)(ButtonAppBar);
