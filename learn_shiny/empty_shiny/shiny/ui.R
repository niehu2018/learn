library(shiny)

# Define UI
ui <- fluidPage(
    titlePanel("Hello Shiny!"),
    sidebarLayout(
        sidebarPanel(),
        mainPanel()
    )
)