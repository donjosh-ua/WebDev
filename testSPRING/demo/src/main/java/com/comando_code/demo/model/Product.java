package com.comando_code.demo.model;

@lombok.Getter
@lombok.Setter
public class Product {
    private Integer id;
    private String name;
    private String description;
    private Double price;
    private Integer ammount;
    private String url_image;

    public Product(Integer id, String name, String description, Double price, Integer ammount, String url_image) {
        this.id = id;
        this.name = name;
        this.description = description;
        this.price = price;
        this.ammount = ammount;
        this.url_image = url_image;
    }

}
