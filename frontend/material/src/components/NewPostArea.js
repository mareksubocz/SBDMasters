import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import TextField from '@material-ui/core/TextField';

const useStyles = makeStyles(theme => ({
  root: {
    '& .MuiTextField-root': {
      marginTop: theme.spacing(1),
      marginBottom: 5,
      // margin: theme.spacing(1),
      width: '100%',
      backgroundColor: 'white',
    },
  },
}));

export default function MultilineTextFields(props) {
  const classes = useStyles();
  const [value, setValue] = React.useState('');

  const handleChange = event => {
    setValue(event.target.value);
    props.onChange(event.target.value);
  };

  return (
    <form className={classes.root} noValidate autoComplete="off">
      <div>
        <TextField
          id="outlined-multiline-static"
          label="Nowa Notatka"
          multiline
          rows="4"
          defaultValue="Default Value"
          variant="outlined"
          placeholder="Napisz o nowej, ciekawej stronie"
          value={value}
          onChange={handleChange}></TextField>
      </div>
    </form>
  );
}
