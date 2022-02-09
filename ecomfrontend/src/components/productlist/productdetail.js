import React, { useState } from "react";
import axios from 'axios';
import { useParams } from "react-router-dom";



export default function Product(){

    const { id } = useParams();
    const rooturl = "http://localhost:8000"
    const [product, setProduct] = React.useState({ product: ''});
    
    let data = "" ;
    axios.get(rooturl+'/api/product-detail/'+id+"/")
    .then(res => {
        data = res.data;
        setProduct({product:data})
    })
    .catch(err => {
        console.log(err)
    })

    return(
        <>
        <br/>
        <div className="container">
            <div className="card mb-4 box-shadow">
                <div className="select2-container--classNameic">
                    <img className="card-img-top" src={rooturl+product.product.image} style={{maxHeight:"350px", width:"auto", display: "block", marginLeft: "auto", marginRight: "auto", marginTop:"10px"}} />
                </div>
                <div className="card-body">
                    <h3 className="card-text">{product.product.name}</h3>
                    <h2 className="card-text" style={{color:"green"}}>{product.product.price +" INR"}</h2>
                    <br/>
                    <p className ="card-text">{product.product.description}</p>
                    <div className="d-flex justify-content-between align-items-center">
                        <div className="btn-group">
                        <a href=""><button type="button" style={{margin:"1px"}} className="btn btn-sm btn-outline-info">ADD TO CART</button></a>
                        <a href=""><button type="button" style={{margin:"1px"}} className="btn btn-sm btn-outline-warning">EDIT</button></a>
                        <a href="" onclick="return confirm('Are you sure you want to delete this item?');" ><button type="button" style={{margin:"1px"}} className="btn btn-sm btn-outline-danger">DELETE</button></a>

                        </div>
                    </div>
                </div>
            </div>
        </div>
        </>
    );
}
