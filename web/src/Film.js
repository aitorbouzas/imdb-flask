import React, { Component } from 'react';
import './Film.css';

class Film extends Component {

  componentDidMount(){
    fetch('http://localhost:5000/api/top/')
    .catch(err => console.error(err))
    .then(res => res.json())
    .then(json => this.setState(json))
  }

  deleteFilm(film){
    fetch('http://localhost:5000/api/film/' + film.id, {
      method: 'DELETE',
    })
    var i = this.state.films.map(function(item) { return item.id; }).indexOf(film.id);
    var new_films = this.state.films.splice(i, 1);
    this.setState(new_films)
  }

  render() {
    if(this.state && this.state.films){
      return(
        <div className="Film">
          <div className="Films">
            <div>
              <h3 align="center">Top 250 IMDB Films</h3>
              <table className="table table-striped">
                <thead>
                  <tr>
                    <th></th>
                    <th>Position</th>
                    <th>Name</th>
                    <th>Year</th>
                    <th>Rating</th>
                    <th></th>
                  </tr>
                </thead>
                <tbody>
                  {
                    this.state.films
                    .sort((a, b) => (a.pos - b.pos))
                    .map((film) => (
                      <tr className="Film-Item" key={"film-"+film.id}>
                        <td><img src={film.image} alt={film.name}/></td>
                        <td>{film.pos}</td>
                        <td><a href={film.url}>{film.name}</a></td>
                        <td>{film.year}</td>
                        <td>{film.rating}</td>
                        <td><button onClick={this.deleteFilm.bind(this, film)}>Delete</button></td>
                      </tr>
                    ))
                  }
                </tbody>
              </table>
            </div>
          </div>
        </div>
      )
    } else {
      return(
        <div className="Error">
          Loading...
        </div>
      )
    }
  }
}

export default Film;
