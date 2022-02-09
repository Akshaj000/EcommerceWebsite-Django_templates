import React from "react";
import {Link} from "react-router-dom";

export default function Card(props){

    const imagestyle = {
        maxHeight:"200px", 
        maxwidth:"300px", 
        width:"auto", 
        display: "block", 
        marginLeft: "auto", 
        marginRight: "auto", 
        marginTop:"10px"
    }

    return(
        <div className="col-md-4">
            <div className="card mb-5 box-shadow">
                <div className="select2-container--classic">
                    <img className="card-img-top" src={props.imageurl} style={imagestyle} />
                </div>
                <div className="card-body">
                    <p className="card-text">{props.name}</p>
                    <h5>{props.price+ " INR"}</h5>
                    <br/>
                    <div className="d-flex justify-content-between align-items-center">
                        <div className="btn-group">
                            <Link to={props.view}><button  type="button" className="btn btn-sm btn-outline-secondary">View</button></Link>
                            <button onClick={props.addtocart} type="button" className="btn btn-sm btn-outline-info updatecart">Add to cart</button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );

}