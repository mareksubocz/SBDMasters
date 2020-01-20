import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import clsx from 'clsx';
import Card from '@material-ui/core/Card';
import CardHeader from '@material-ui/core/CardHeader';
// import CardMedia from '@material-ui/core/CardMedia';
import CardContent from '@material-ui/core/CardContent';
import CardActions from '@material-ui/core/CardActions';
import Collapse from '@material-ui/core/Collapse';
import Avatar from '@material-ui/core/Avatar';
import IconButton from '@material-ui/core/IconButton';
import Typography from '@material-ui/core/Typography';
// import { red } from '@material-ui/core/colors';
// import FavoriteIcon from '@material-ui/icons/Favorite';
import TextField from '@material-ui/core/TextField';
import ShareIcon from '@material-ui/icons/Share';
import ExpandMoreIcon from '@material-ui/icons/ExpandMore';
import MoreVertIcon from '@material-ui/icons/MoreVert';
import avatar from '../img/maciek.jpeg'
import LikeIcon from '@material-ui/icons/ThumbUp'
import { Button } from '@material-ui/core';
import Comment from './Comment'

const useStyles = makeStyles(theme => ({
    card: {
        maxWidth: 345,
    },
    media: {
        height: 0,
        paddingTop: '56.25%', // 16:9
    },
    expand: {
        transform: 'rotate(0deg)',
        marginLeft: 'auto',
        color: 'grey',
        fontSize: '15px',
        transition: theme.transitions.create('transform', {
            duration: theme.transitions.duration.shortest,
        }),
    },
    expandOpen: {
        // transform: 'rotate(180deg)',
    },
    avatar: {
    },
    writeComment: {
        // marginBottom: '-10'
    }
}));

export default function NoteCard() {
    const classes = useStyles();
    const [expanded, setExpanded] = React.useState(false);

    const handleExpandClick = () => {
        setExpanded(!expanded);
    };

    return (
        <Card className={classes.card}>
            <CardHeader
                avatar={
                    <Avatar alt="Maciek" src={avatar} className={classes.avatar} />
                }
                action={
                    <IconButton aria-label="settings">
                        <MoreVertIcon />
                    </IconButton>
                }
                title="Maćko z Bogdańca, id: "
                subheader="September 14, 2016"
            />
            {/* <CardMedia
        className={classes.media}
        image={avatar}
        title="Paella dish"
      /> */}
            <CardContent>
                <Typography variant="body2" color="textSecondary" component="p">
                    Zobaczcie jaki fajny link <a href='www.example.com'>example</a>
                </Typography>
            </CardContent>
            <CardActions disableSpacing>
                <IconButton aria-label="add to favorites">
                    <LikeIcon />
                </IconButton>
                <IconButton aria-label="share">
                    <ShareIcon />
                </IconButton>
                <Button className={clsx(classes.expand, {
                    [classes.expandOpen]: expanded,
                })}
                    onClick={handleExpandClick}
                    aria-expanded={expanded}
                    aria-label="show more"
                >
                    Comments
                    <ExpandMoreIcon />
                </Button>
            </CardActions>
            <Collapse in={expanded} timeout="auto" unmountOnExit>
                <CardContent className={classes.writeComment}>
                    <Comment></Comment>
                    <Comment></Comment>
                    <TextField fullWidth label="Write a Comment" />
                </CardContent>
            </Collapse>
        </Card >
    );
}
