$(function() {

  function showSeries() {

      $.ajax({
          url: "http://localhost:5000/get-series",
          method: "GET",
          dataType: "json", 
          success: listSeries, 
          error: function() {
              alert("erro ao ler dados, verifique o backend");
          },
      });

      function listSeries(series) {
          $("#tableBody").empty();
          showContent("tabela-serie");
          for (serie of series) {

              var newRow = `<tr id="line_${serie.id}"> 
                              <td>${serie.nome}</td> 
                              <td>${serie.genero}</td> 
                              <td>${serie.numtemps}</td> 
                              <td>${serie.nota}</td> 
                              <td>
                                  <a href="#" id="delete_${serie.id}" class="delete_serie" title="Excluir Série">
                                          deletar
                                  </a>
                              </td>
                            </tr>`;

              $("#tableBody").append(newRow);
          }
      }
  }


  function showContent(nextPage) {
      $("#inicio").addClass("invisible");
      $("#tabela-serie").addClass("invisible");
      $(`#${nextPage}`).removeClass("invisible");
  }

  $("#link-listar").click(function() {
      showSeries();
  });

  $("#link-inicial").click(function() {
      showContent("inicio");
  });

  $("#nav-brand").click(function() {
      showContent("inicio");
  });

  $(document).on("click", "#btn-incluir", function() {
      const nome = $("#campo-nome").val();
      const genero = $("#campo-genero").val();
      const numtemps = $("#campo-numtemps").val();
      const nota = $("#campo-nota").val();

      const serieData = JSON.stringify({
          nome: nome,
          genero: genero,
          numtemps: numtemps,
          nota: nota,
      });

      $.ajax({
          url: "http://localhost:5000/create-series",
          type: "POST",
          dataType: "json",
          contentType: "application/json",
          data: serieData,
          success: createdSerie,
          error: createdSerieError,
      });

      function createdSerie(resposta) {
          if (resposta.result == "ok") {
              $("#campo-nome").val("");
              $("#campo-genero").val("");
              $("#campo-numtemps").val("");
              $("#campo-nota").val("");
              showSeries();
              alert("Serie adicionada com sucesso");
              $(".close").click();

          } else {
              alert(resposta.result + ':' + resposta.details);
          }
      }


      function createdSerieError(resposta) {
          alert("Erro na chamada do back-end");
      }
  });

  $('#modal-incluir').on('hidden.bs.modal', function(e) {
      if (!$('#tabela-serie').hasClass('invisible')) {
          showSeries();
      }
  });

  showContent("inicio");

  $(document).on("click", ".delete_serie", function() {
      var component = $(this).attr("id");

      var icon_name = "delete_";
      var serie_id = component.substring(icon_name.length);

      $.ajax({
          url: 'http://localhost:5000/delete-series/' + serie_id,
          type: "DELETE",
          dataType: "json",
          success: deletedSerie,
          error: deletedSerieError
      });

      function deletedSerie(retorno) {
          if (retorno.result == "ok") {
              $('#line_' + serie_id).fadeOut(1000, function() {
                  alert("Serie Removida com Sucesso!");
                  showSeries();
              });
          } else {
              alert(`${retorno.result}: ${retorno.details}`);
          }
      }

      function deletedSerieError(response) {
          alert("Erro ao excluir dados, verifique o Backend!");
      }
  });

});