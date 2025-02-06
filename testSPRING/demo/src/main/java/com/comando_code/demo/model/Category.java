package com.comando_code.demo.model;

import java.util.Map;

@lombok.Getter
@lombok.Setter
public class Category {
    private String name;
    private Map<Integer, Product> products;

    public Category(String name) {
        this.name = name;
        this.products = new java.util.HashMap<>();
    }

    public void addProduct(Integer id, Product product) {
        this.products.put(id, product);
    }

    public void removeProduct(Integer id) {
        this.products.remove(id);
    }
}
