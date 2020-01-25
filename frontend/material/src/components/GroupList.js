import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import GridList from '@material-ui/core/GridList';
import GridListTile from '@material-ui/core/GridListTile';
import maciek from '../img/maciek.jpeg';
import maciek2 from '../img/maciek2.jpg';
import Group from './Group';

const useStyles = makeStyles(theme => ({
  root: {
    display: 'flex',
    flexWrap: 'wrap',
    justifyContent: 'space-around',
    overflow: 'hidden',
    backgroundColor: theme.palette.background.paper,
  },
  gridList: {
    maxWidth: 360,
    // height: 450,
  },
}));




const tileData = [
  {
    // img: maciek,
    title: 'Imagedsa',
    author: 'authorek',
    cols: 1,
  },
  {
    img: maciek2,
    title: 'Imadsage',
    author: 'author',
    cols: 1,
  },
  {
    img: maciek,
    title: 'Imasge',
    author: 'authorwdw',
    cols: 1,
  },
  {
    img: maciek2,
    title: 'Imaage',
    author: 'author',
    cols: 2,
  },
  {
    img: maciek,
    title: 'Image',
    author: 'author',
    cols: 1,
  },
  {
    img: maciek2,
    title: 'Image',
    author: 'author',
    cols: 2,
  },
  {
    img: maciek,
    title: 'Image',
    author: 'author',
    cols: 1,
  },
  {
    img: maciek2,
    title: 'Image',
    author: 'author',
    cols: 1,
  },
  {
    img: maciek,
    title: 'Image',
    author: 'author',
    cols: 1,
  },
  {
    img: maciek2,
    title: 'Image',
    author: 'author',
    cols: 1,
  },
  {
    img: maciek,
    title: 'Image',
    author: 'author',
    cols: 2,
  },
  {
    img: maciek2,
    title: 'Image',
    author: 'author',
    cols: 1,
  },
  {
    img: maciek,
    title: 'Image',
    author: 'author',
    cols: 1,
  },
  {
    img: maciek2,
    title: 'Ponczek',
    author: 'author',
    inside: '#costam #tamto',
    cols: 1,
  },
  {
    img: maciek,
    title: 'Image',
    subtitle: 'author',
    cols: 1,
  },
  {
    img: maciek2,
    title: 'Image',
    author: 'author',
    cols: 1,
  },
];

export default function ImageGridList(props) {
  const classes = useStyles();

  return (
    <div className={classes.root}>
      <GridList cellHeight={160} className={classes.gridList} cols={3}>
        {/* props.tileData */}
        {tileData.map(tile => (
          <GridListTile key={tile.img} cols={tile.cols || 1}>
            {/* <img src={tile.img} alt={tile.title} /> */}
            <Group {...tile}></Group>
          </GridListTile>
        ))}
      </GridList>
    </div >
  );
}
