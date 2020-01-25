import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import Card from '@material-ui/core/Card';
import CardHeader from '@material-ui/core/CardHeader';
import CardContent from '@material-ui/core/CardContent';
import Typography from '@material-ui/core/Typography';

const useStyles = makeStyles(theme => ({
  card: {
    // maxWidth: 345,
    backgroundColor: '#f0f0f5',
    marginBottom: 5,
  },
  inside: {
    padding: 10,
  },
  content: {
    padding: 10,
    paddingTop: 0,
    // paddingBottom: 0,
    marginBottom: -10,
  },
  like: {
    size: 'small'
  },
}));

export default function GroupCard(props) {
  const classes = useStyles();

  return (
    <Card className={classes.card}>
      <CardHeader className={classes.inside}
        title={props.title}
        subheader={props.subtitle}
      />
      <CardContent fullWidth className={classes.content}>
        <Typography variant="body2" color="textSecondary" component="p">
          {props.inside}
        </Typography>
      </CardContent>
    </Card >
  );
}
