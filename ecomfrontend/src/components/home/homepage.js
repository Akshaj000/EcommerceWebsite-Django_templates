import React from "react";
import Card from "./card";
import axios from 'axios';
import {updateProductstate} from "../productlist/productdetail";

class Homepage extends React.Component {

    rooturl = "http://localhost:8000"

    constructor(props) {
        super(props);
        this.state = {
            productlist : []
        }
    }

    componentDidMount() {
  
        let data ;
        axios.get(this.rooturl+'/api/product-list/')
        .then(res => {
            data = res.data;
            this.setState({
                productlist : data   
            });
        })
        .catch(err => {
            console.log(err)
        })
        
    }

    render(){

        let products = []
        const productlist = this.state.productlist
        for( let i=0; i<productlist.length;i++){
            products.push(
                <Card view={"product/"+productlist[i].id+"/"} imageurl={this.rooturl+productlist[i].image} name={productlist[i].name} price={productlist[i].price}/>
            )
        }

        return (
            <main role="main">
                <div className="album py-5 bg-light">
                    <div className="container">
                        <div className="row">
                            {products}
                        </div>
                    </div>
                </div>
            </main>
        );
        

    }
}

export default Homepage


