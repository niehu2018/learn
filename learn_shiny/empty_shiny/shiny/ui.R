library(shiny)

# Define UI
ui <- fluidPage(
    titlePanel("title panel"),
    
    sidebarLayout(
        sidebarPanel("sidebar panel"),
        mainPanel("main panel")
    )
)