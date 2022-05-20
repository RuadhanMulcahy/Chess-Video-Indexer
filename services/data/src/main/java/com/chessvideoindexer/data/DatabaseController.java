package com.chessvideoindexer.data;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.*;

@Controller
@RequestMapping(path="/db")
public class DatabaseController {
    @Autowired
    private ChessGameRepository chessGameRepository;

    @PostMapping(path="/add")
    public @ResponseBody String addNewChessGame(@RequestParam String url) {
        ChessGame chessGame = new ChessGame();
        chessGame.setUrl(url);
        chessGameRepository.save(chessGame);
        return "Game saved";
    }

    @GetMapping(path="/all")
    public @ResponseBody Iterable<ChessGame> getAllChessGames() {
        return chessGameRepository.findAll();
    }
}
