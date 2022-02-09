import React from "react";
import Header from "./base/header"
import Footer from "./base/footer"
import Homepage from "./components/home/homepage";
import {
  BrowserRouter, 
  Routes, 
  Route 
} from "react-router-dom";
import Product from "./components/productlist/productdetail";

class Site extends React.Component{

  render(){

    return (
      <BrowserRouter>
        <Header/>
        <Routes>
          <Route exact path='/' element={<Homepage/>}/>
          <Route exact path='/product/:id' element={<Product/>}/>
        </Routes>
       <Footer/>
      </BrowserRouter>
    );
  }
}

export default Site;
