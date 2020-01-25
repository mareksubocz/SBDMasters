import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import Card from '@material-ui/core/Card';
import CardHeader from '@material-ui/core/CardHeader';
import CardContent from '@material-ui/core/CardContent';
import Avatar from '@material-ui/core/Avatar';
import IconButton from '@material-ui/core/IconButton';
import Typography from '@material-ui/core/Typography';
import avatar from '../img/maciek.jpeg'
import LikeIcon from '@material-ui/icons/ThumbUp'

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
  avatar: {
  },
  like: {
    size: 'small'
  },
}));

export default function CommentCard(props) {
  const classes = useStyles();
  // const [expanded, setExpanded] = React.useState(false);

  // const handleExpandClick = () => {
  //   setExpanded(!expanded);
  // };

  return (
    <Card className={classes.card}>
      <CardHeader className={classes.inside}
        avatar={
          <Avatar alt={props.user} src={avatar} className={classes.avatar} />
        }
        action={
          <IconButton aria-label="add to favorites" className={classes.like}>
            <LikeIcon />
          </IconButton>
        }
        title={props.user}
        subheader={props.date}
      />
      <CardContent fullWidth className={classes.content}>
        <Typography variant="body2" color="textSecondary" component="p">
          {props.content}
        </Typography>
      </CardContent>
    </Card >
  );
}
